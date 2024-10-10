# 가장 아래에 있는 요소만 움직인다. 라는 조건이 빠진다
# https://www.acmicpc.net/problem/17837

import sys


class Piece:
    def __init__(self, no, direction):
        self.no = no
        self.direction = direction


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def opposite(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    return 2


'''
def go(a, where, x, y, nx, ny):
    for p in a[x][y]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny)
    a[x][y].clear()

    가장 아래에 있는 애만 움직인다
    따라서, 모두가 같은 방향으로 움직이는 코드 
'''


def go(a, where, x, y, nx, ny, start):
    # start 번째부터 이동할 수 있게 해주었다
    # 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다
    # 즉, start 지점 그 위의 말들을 모두 이동시켜주는 것이다
    for i in range(start, len(a[x][y])):
        p = a[x][y][i]
        a[nx][ny].append(p)
        # len(a[nx][ny])-1 : 위치(해당 행,열에서 몇번째)
        where[p.no] = (nx, ny, len(a[nx][ny])-1)
    a[x][y] = a[x][y][:start]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m

for i in range(m):
    x, y, direction = map(int, input().split())
    a[x-1][y-1].append(Piece(i, direction-1))
    # 새로운 게임1 에서는 (행,열)위치만 중요했다
    # 하지만, 이제는 해당 위치에서 , 몇번째에 쌓여있는지도 알아야 한다
    where[i] = (x-1, y-1, len(a[x-1][y-1])-1)

for turn in range(1, 1001):
    for k in range(m):
        x, y, index = where[k]
        direction = a[x][y][index].direction
        nx = x+dx[direction]
        ny = y+dy[direction]
        if 0 <= nx < n and 0 <= ny < n:  # in
            if board[nx][ny] == 2:
                a[x][y][index].direction = opposite(direction)
        else:
            a[x][y][index].direction = opposite(direction)
        direction = a[x][y][index].direction
        # updata 한 방향에 근거한, 새로운 위치
        nx = x+dx[direction]
        ny = y+dy[direction]

        if 0 <= nx < n and 0 <= ny < n:  # in
            if board[nx][ny] == 0:
                go(a, where, x, y, nx, ny, index)
            elif board[nx][ny] == 1:
                a[x][y] = a[x][y][:index] + a[x][y][index:][::-1]
                go(a, where, x, y, nx, ny, index)
            if len(a[nx][ny]) >= 4:
                print(turn)
                sys.exit(0)
        else:  # out
            pass
print(-1)

'''
>> 1번째 풀이
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <climits>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;

int N, K;
int dRow[]	= { 0, 0, -1, 1 }; // 오,왼,위,아
int dCol[]	= { 1, -1, 0, 0 };
struct Horse
{
	int r, c, dir, n;
};
enum class KAN
{
	WHITE,
	RED,
	BLUE
};
// 여러 Horse, [0] 가 가장 밑. 말 숫자
vector<vector<vector<int>>> Chess;
vector<vector<KAN>> Map;
vector<Horse> HorseMap;

int getOpdir(int dir)
{
	if (dir == 0) return 1;
	if (dir == 1) return 0;
	if (dir == 2) return 3;
	if (dir == 3) return 2;
}

void Input()
{
	cin >> N >> K;
	HorseMap.resize(K);
	Chess.resize(N, vector<vector<int>>(N));
	Map.resize(N, vector<KAN>(N));

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			int kan;
			cin >> kan;
			Map[i][j] = (KAN)kan;
		}
	}

	for (int k = 0; k < K; ++k)
	{
		int r, c, dir;
		cin >> r >> c >> dir;
		Horse horse = { r - 1, c - 1, dir - 1, k};
		Chess[r-1][c-1].push_back(k);
		HorseMap[k] = horse;
	}
}

bool moveRed(int oldR, int oldC, int nxtR, int nxtC, int curIdx)
{
	// HorseMap 정보도 update 한다.
	// Chess 판에서 현재 칸에 있는 모든 내용을 순서반대로 올린다.
	for (int idx = Chess[oldR][oldC].size() - 1;
		idx >= curIdx; --idx)
	{
		int horseNum = Chess[oldR][oldC][idx];
		HorseMap[horseNum].r = nxtR;
		HorseMap[horseNum].c = nxtC;
		Chess[nxtR][nxtC].push_back(Chess[oldR][oldC][idx]);
	}
	
	Chess[oldR][oldC].erase(Chess[oldR][oldC].begin() + curIdx, 
		Chess[oldR][oldC].end());
	
	if (Chess[nxtR][nxtC].size() >= 4)
		return false;

	return true;
}

bool moveWhite(int oldR, int oldC, int nxtR, int nxtC, int curIdx)
{
	// HorseMap 정보도 update 한다.
	// Chess 판에서 현재 칸에 있는 모든 내용을 그대로 올린다.
	for (int idx = curIdx; idx < Chess[oldR][oldC].size(); ++idx)
	{
		int horseNum = Chess[oldR][oldC][idx];
		HorseMap[horseNum].r = nxtR;
		HorseMap[horseNum].c = nxtC;
		Chess[nxtR][nxtC].push_back(Chess[oldR][oldC][idx]);
	}

	if (Chess[nxtR][nxtC].size() >= 4)
		return false;

	Chess[oldR][oldC].erase(Chess[oldR][oldC].begin() + curIdx, 
		Chess[oldR][oldC].end());
	return true;
}

void Solve()
{
	// 말 위에 말을 올릴 수 있음
	// white, red, blue
	// 1. 말 이동
	// - 흰색 : 이동 -> 그냥 쌓아올리기
	// - 빨간색 : 이동 + 순서 반대로 변경. 로직 상으로는 현재 애들 순서 변경
	//   그 다음 칸 위에 쌓아올리기
	// - 파란색
	//   방향 반대로 
	//   이동 칸이 파란색이면, 이동 X
	//   그게 아니라면, 이동
	// - 벗어남
	//   파란색과 같은 로직 적용하기

	// r,c 탐색
	// 2개 이상일 수 있잖아.
	// 그러면 재귀 ? 로 더이상 이동할 말이 없을 때까지 반복하자.
	int turn = 1;

	while (turn <= 1000)
	{
		bool end = false;
		for (int k = 0; k < K; ++k)
		{
			Horse curHorse = HorseMap[k];
			int oldR = curHorse.r;
			int oldC = curHorse.c;
			int nxtR = curHorse.r + dRow[curHorse.dir];
			int nxtC = curHorse.c + dCol[curHorse.dir];
			int curIdx = -1;

			for (int idx = 0; idx < Chess[oldR][oldC].size(); ++idx)
			{
				if (Chess[oldR][oldC][idx] == k)
				{
					curIdx = idx;
					break;
				}
			}

			// 범위 벗어나는 가
			if (nxtR < 0 || nxtR >= N || nxtC < 0 || nxtC >= N)
			{
				curHorse.dir = getOpdir(curHorse.dir);
				nxtR = oldR + dRow[curHorse.dir];
				nxtC = oldC + dCol[curHorse.dir];
				KAN nxtKan = Map[nxtR][nxtC];
				HorseMap[k].dir = curHorse.dir;
				// 이동
				if (nxtKan == KAN::RED)
				{
					if (!moveRed(oldR, oldC, nxtR, nxtC, curIdx))
					{
						end = true;
						break;
					}
				}
				else // WHITE
				{
					if (!moveWhite(oldR, oldC, nxtR, nxtC, curIdx))
					{
						end = true;
						break;
					}
				}
			}
			else
			{
				KAN nxtKan = Map[nxtR][nxtC];
				if (nxtKan == KAN::BLUE)
				{
					curHorse.dir = getOpdir(curHorse.dir);
					nxtR = oldR + dRow[curHorse.dir];
					nxtC = oldC + dCol[curHorse.dir];
					HorseMap[k].dir = curHorse.dir;
					if (nxtR >= 0 && nxtR < N && nxtC >= 0 && nxtC < N)
					{
						nxtKan = Map[nxtR][nxtC];
						// 이동
						// 1) 빨강
						// 2) 흰색
						if (nxtKan == KAN::RED)
						{
							if (!moveRed(oldR, oldC, nxtR, nxtC, curIdx))
							{
								end = true;
								break;
							}
						}
						else // WHITE
						{
							if (!moveWhite(oldR, oldC, nxtR, nxtC, curIdx))
							{
								end = true;
								break;
							}
						}
					}
				}
				else if (nxtKan == KAN::RED)
				{
					if (!moveRed(oldR, oldC, nxtR, nxtC, curIdx))
					{
						end = true;
						break;
					}
				}
				else // WHITE
				{
					if (!moveWhite(oldR, oldC, nxtR, nxtC, curIdx))
					{
						end = true;
						break;
					}
				}
			}
		}
		if (end)
			break;
		turn += 1;
	}

	if (turn > 1000)
		cout << -1 << endl;
	else
		cout << turn << endl;
}

int main() {
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}

'''

'''
>> 정답 풀이
C++

#include <iostream>
#include <tuple>
#include <algorithm>
#include <vector>
using namespace std;
int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};
int opposite(int dir) {
    if (dir == 0) return 1;
    if (dir == 1) return 0;
    if (dir == 2) return 3;
    return 2;
}
void go(vector<vector<vector<pair<int,int>>>> &a, 
vector<tuple<int,int,int>> &where, int x, int y, int nx, int ny, 
int start) {
    for (int i=start; i<a[x][y].size(); i++) {
        auto &p = a[x][y][i];
        a[nx][ny].push_back(p);
        where[p.first] = make_tuple(nx, ny, (int)a[nx][ny].size()-1);
    }
    a[x][y].resize(start);
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> board[i][j];
        }
    }
    vector<vector<vector<pair<int,int>>>> a(n, 
        vector<vector<pair<int,int>>>(n));
    vector<tuple<int,int,int>> where(m);
    for (int i=0; i<m; i++) {
        int x, y, dir;
        cin >> x >> y >> dir;
        a[x-1][y-1].push_back(make_pair(i, dir-1));
        where[i] = make_tuple(x-1, y-1, (int)a[x-1][y-1].size()-1);
    }
    for (int turn=1; turn<=1000; turn++) {
        for (int k=0; k<m; k++) {
            int x, y, index;
            tie(x,y,index) = where[k];
            int dir = a[x][y][index].second;
            int nx = x+dx[dir];
            int ny = y+dy[dir];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                if (board[nx][ny] == 2) {
                    a[x][y][index].second = opposite(dir);
                }
            } else {
                a[x][y][index].second = opposite(dir);
            }
            dir = a[x][y][index].second;
            nx = x+dx[dir];
            ny = y+dy[dir];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                if (board[nx][ny] == 0) {
                    go(a, where, x, y, nx, ny, index);
                } else if (board[nx][ny] == 1) {
                    reverse(a[x][y].begin()+index, a[x][y].end());
                    go(a, where, x, y, nx, ny, index);
                }
                if (a[nx][ny].size() >= 4) {
                    cout << turn << '\n';
                    return 0;
                }
            } else { // out
            }
        }
    }
    cout << -1 << '\n';
    return 0;
}

'''
