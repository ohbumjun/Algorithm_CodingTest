// https://www.acmicpc.net/problem/13460

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

int answer = 11;
int N, M; // 세로,가로 크기

int dRow[4] = { -1, 1, 0, 0 }; // 위, 아, 왼, 오
int dCol[4] = { 0, 0, -1, 1 };

int outRow, outCol;
int redRow, redCol;
int blueRow, blueCol;
vector<vector<bool>> board;	// false : 방문 불가

// out : 움직이는 와중에 빠질 수 있다.
pair<int,int> findNext(int row, int col, int d, 
	vector<vector<bool>>& cBoard, bool& out)
{
	pair<int,int> nextPos = { row, col };
	int curRow = row;
	int curCol = col;
	while (true)
	{
		int nextRow = curRow + dRow[d];
		int nextCol = curCol + dCol[d];

		if (nextRow == outRow && nextCol == outCol)
		{
			out = true;
			return { row, col };
		}

		if (nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= M)
			break;

		if (board[nextRow][nextCol] == false)
			break;

		curRow = nextRow;
		curCol = nextCol;
	}

	nextPos = { curRow, curCol };

	return nextPos;
}

// cnt : 지금까지 움직인 횟수
void dfs(int cnt, int rRow, int rCol, int bRow, int bCol, 
	vector<vector<bool>>& cBoard)
{
	if (cnt >= 10)
		return;

	// 상하 좌우 움직이기
	for (int d = 0; d < 4; ++d)
	{
		bool same = false;

		bool redOut = false, blueOut = false;
		pair<int, int> redNext = findNext(rRow, rCol, d, cBoard, redOut);
		pair<int, int> blueNext = findNext(bRow, bCol, d, cBoard, blueOut);

		if (redOut && blueOut)
		{
			// 동시에 빠지면 실패한 케이스
			continue;
		}
		else if (blueOut)
		{
			// 파란색이 빠진 경우는 실패
			continue;
		}
		else if (redOut)
		{
			// 빨간색이 빠진 경우
			answer = min(answer, cnt + 1);
			break;
		}

		bool redFix = redNext.first == rRow && redNext.second == rCol;
		bool blueFix = blueNext.first == bRow && blueNext.second == bCol;

		if (redNext.first == blueNext.first && redNext.second == blueNext.second)
		{
			same = true;
			
			// 동시에 빠진 경우는 실패.
			if (redNext.first == outRow && redNext.second == outCol)
				continue;
		}
		else
		{
			// 빨간색이 빠진 경우
			if (redNext.first == outRow && redNext.second == outCol)
			{
				// 더이상 다른 방향으로 진행할 필요 없는 것 아닐까 ?
				// 그러면 현재 dfs 루프를 빠져나가면 될 것 같다.
				answer = min(answer, cnt + 1);
				break;;
			}
		}

		// 2개의 공이 같은 위치에 있게 될 경우
		if (same)
		{

			switch (d)
			{
			case 0: // 위
				// 공이 같은 col 에 있는지 확인
				// 더 위에 있는 공을 먼저 위로 이동
				if (rCol == bCol)
				{
					if (rRow < bRow)
					{
						// 파란색이 더 아래에 있었다면, blueNext row 증가
						blueNext.first += 1;
					}
					else
					{
						// 빨간색이 더 아래에 있었다면, redNext row 증가
						redNext.first += 1;
					}
				}
				break;
			case 1: // 아
				// 공이 같은 col 에 있는지 확인
				// 더 아래에 있는 공을 먼저 아래로 이동
				if (rCol == bCol)
				{
					if (rRow < bRow)
					{
						// 빨간색이 더 위에 있었다면, redNext row 감소
						redNext.first -= 1;
					}
					else
					{
						// 파란색이 더 위에 있었다면, blueNext row 감소
						blueNext.first -= 1;
					}
				}
				break;
			case 2:	// 왼
				// 공이 같은 row 에 있는지 확인
				// 더 왼쪽에 있는 공을 먼저 왼쪽으로 이동

				if (rRow == bRow)
				{
					if (rCol < bCol)
					{
						// 파란색이 더 오른쪽에 있었다면, blueNext col 증가
						blueNext.second += 1;
					}
					else
					{
						// 빨간색이 더 오른쪽에 있었다면, redNext col 증가
						redNext.second += 1;
					}
				}
				break;
			case 3:	// 오
				// 공이 같은 row 에 있는지 확인
				// 더 오른쪽에 있는 공을 먼저 오른쪽으로 이동
				if (rRow == bRow)
				{
					if (rCol < bCol)
					{
						// 빨간색이 더 왼쪽에 있었다면, redNext col 감소
						redNext.second -= 1;
					}
					else
					{
						// 파란색이 더 왼쪽에 있었다면, blueNext col 감소
						blueNext.second -= 1;
					}
				}
				break;
			}
		}

		// 둘다 fix 인 경우는 그냥 cnt 만 증가시키고 다음으로 넘어간다.
		if (redFix && blueFix)
		{
			dfs(cnt + 1, rRow, rCol, bRow, bCol, cBoard);
		}
		else
		{
			// 변경된 위치 기준으로 dfs
			dfs(cnt + 1, redNext.first, redNext.second, blueNext.first, blueNext.second, cBoard);
		}

	}
}

void Input()
{
	cin >> N >> M;
	board.resize(N, vector<bool>(M, true));

	for (int n = 0; n < N; ++n)
	{
		for (int m = 0; m < M; ++m)
		{
			char c;
			cin >> c;
			switch (c)
			{
			case '#' :
				board[n][m] = false;
				break;
			case 'O' :
				outRow = n;
				outCol = m;
				break;
			case 'R' :
				redRow = n;
				redCol = m;
				break;
			case 'B' :
				blueRow = n;
				blueCol = m;
				break;
			}
		}
	}
	
}

void Solve()
{
	// 빨간 구슬 빼내기
	// 파란 구슬, 빨간 구슬 1개씩
	// 파란 구슬이 구멍에 들어가면 안됨
	// 파란 구슬, 빨간 구슬 동시에 빠져도 실패
	// 파란 구슬, 빨간 구슬 동시에 같은 카에 있지 못한다.
	// 더이상 구슬이 움직이지 못하면 기욱이는 동작 못함
	// 최소 몇번 만에 빨간 구슬 빼낼 수 있는가
	dfs(0, redRow, redCol, blueRow, blueCol, board);

	if (answer == 11)
		cout << -1 << endl;
	else 
		cout << answer << endl;
}

/*
(0)
0 4  4   32
4 0  2   64
8 8  0   0
0 16 64 4

(1)
4 4   4   32
8 8   2   64
0 16 64   0
0 0   0 4
* 
*/

int main() {
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}
