// https://www.acmicpc.net/problem/15685

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

int N;
int dRow[] = {0, -1, 0, 1}; // 동,북,서,남
int dCol[] = {1, 0, -1, 0};
bool map[101][101][4]; // 4방향 (동,북,서,남)

int getOpDir(int cDir)
{
	if (cDir == 0) return 2;
	if (cDir == 1) return 3;
	if (cDir == 2) return 0;
	if (cDir == 3) return 1;
}

int get90RightDir(int cDir)
{
	if (cDir == 0) return 3;
	if (cDir == 1) return 0;
	if (cDir == 2) return 1;
	if (cDir == 3) return 2;
}

pair<int, int> move(int stR, int stC, int dir)
{
	int nR = stR + dRow[dir];
	int nC = stC + dCol[dir];

	// 격자 밖으로 벗어나지 않는다.
	if (nR == stR)
	{
		int maxC = max(stC, nC);
		if (nR >= 0)
			map[nR][maxC][3] = true; // 윗변 (위칸의 아래쪽)
		if (nR + 1 <= 100)
			map[nR + 1][maxC][1] = true; // 아랫변 (아래칸의 위쪽)
	}

	if (nC == stC)
	{
		// 왼, 오 칠해주기
		int maxR = max(stR, nR);
		if (nC >= 0)
			map[maxR][nC][0] = true; // 왼변 (왼쪽 칸의 오른쪽)
		if (nC + 1 <= 100)
			map[maxR][nC + 1][2] = true; // 오른변 (오른쪽 칸의 왼쪽)
	}

	return {nR, nC};
}

// 특정 시작점에서 curve 를 만들어내는 함수
void makeCurve(int curGen, int targetGen, int stR, int stC,
	vector<int>& accDirs)
{
	if (curGen > targetGen)
		return;
	// curve 목록을 이용해서 좌표에 표시를 해야 한다.
	// curGen 이 0 이면 d 방향으로 stR, stC 에서 1만큼 긋기
	// 그 다음 이제 다음 makeCurve ? 로 넘어감. 방향 변경
	
	// 1 이면, 해당 방향으로 1만큼 긋기
	// 그 다음 makeCurve
	// 2 -> 자. 긋기를 2번 해야 한다.
	// 긋는 함수를 따로 만들어야 할 것 같다.
	// 긋는 함수는 긋고, 표기하고, 도달 위치를 리턴
	
	// 이전 세대에서 와온 방향 정보도 vector 로
	// 새로운 세대에서는 그 방향에 반시계 90 도 방향으로 나아가기

	// 새루운 세대에서는, 지금까지 와온 방향을 모두 시간 방향으로 돌리기
	// 그리고 그 방향의 반대로 돌리기
	// 그 다음, 뒤에서부터 역순 방향을 이용하여 이동한다.
	if (curGen == 0)
	{
		int d = accDirs[0];
		accDirs.pop_back();
		const pair<int, int>& nextPos = move(stR, stC, d);
		accDirs.push_back(d);
		makeCurve(curGen + 1, targetGen,nextPos.first, nextPos.second, accDirs);
		return;
	}

	vector<int> newDirs;
	for (int i = accDirs.size() - 1; i >= 0; --i)
	{
		// int newDir = get90RightDir(accDirs[i]);
		// newDir = getOpDir(newDir);
		// newDirs.push_back(newDir);

		// 사실상 서쪽...
		newDirs.push_back((accDirs[i] + 1) % 4);
	}

	int curR = stR, curC = stC;
	for (int i = 0; i < newDirs.size(); ++i)
	{
		const pair<int, int>& nextPos = move(curR, curC, newDirs[i]);
		curR = nextPos.first;
		curC = nextPos.second;
	}

	vector<int> nextDirs;
	for (int i = 0; i < accDirs.size(); ++i)
		nextDirs.push_back(accDirs[i]);
	for (int i = 0; i < newDirs.size(); ++i)
		nextDirs.push_back(newDirs[i]);

	makeCurve(curGen + 1, targetGen, curR, curC, nextDirs);
}

int checkSquare()
{
	int check = 0;
	for (int r = 0; r < 101; ++r)
	{
		for (int c = 0; c < 101; ++c)
		{
			// 변 3개 이상 칠해져 있으면 된다.
			int cnt = 0;

			if (map[r][c][0]) cnt++;
			if (map[r][c][1]) cnt++;
			if (map[r][c][2]) cnt++;
			if (map[r][c][3]) cnt++;

			if (cnt >= 3)
			{
				check++;
			}
			else if (cnt == 2)
			{
				// 반대 방향에 있는 거라면 +
				if (map[r][c][0] && map[r][c][2])
					check++;
				else if (map[r][c][1] && map[r][c][3])
					check++;
			}
		}
	}


	return check;
} 

void Input()
{
	cin >> N;

	for (int r = 0; r < 101; ++r)
		for (int c = 0; c < 101; ++c)
			for (int d = 0; d < 4; ++d)
				map[r][c][d] = false;
	
	for (int n = 0; n < N; ++n)
	{
		int c, r, d, g;
		cin >> c >> r >> d >> g;
		vector<int> accDirs;
		accDirs.push_back(d);
		makeCurve(0, g, r, c, accDirs);

	}
}

void Solve()
{
	cout << checkSquare() << endl;
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

// 정답 코드 (2번째 풀이)
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

int N;

// 1번째 풀이와 차이점
// 1번째 : Map[101][101] 은 하나의 칸 개념. 4변을 모두 표현
// 정답 : 그냥 말 그대로 꼭짓점으로 표현
int Map[101][101];
int cnt = 0;
int dx[4] = { 1, 0, -1, 0 }; // 동, 북, 서, 남
int dy[4] = { 0, -1, 0, 1 };
int main() {
	ios_base::sync_with_stdio(false);
	//freopen("input.txt", "rt", stdin);
	
	int i, j, n, k;
	int x, y, d, g;

	cin >> N;

	for (i = 0; i < N; i++) {
		cin >> x >> y >> d >> g;
		vector<int> dir;
		dir.push_back(d);
		for (n = 1; n <= g; n++) {
			for (j = dir.size()-1; j >= 0; j--) {
				dir.push_back((dir[j] + 1) % 4);
			}
		}

		Map[y][x] = 1;
		for (k = 0; k < dir.size(); k++) {
			y = y + dy[dir[k]];
			x = x + dx[dir[k]];
			Map[y][x]++;
		}
	}

	for (i = 0; i < 100; i++) { // 여기서 101 이 되면 안된다.
		// 결국은, 맨 마지막 + 1은, 3x3 이라고 하면, 3x3 을 넘어서
		// 오른쪽 아래에 있는 격자 하나를 더 고려하는 꼴이 되기 때문이다.
		for (j = 0; j < 100; j++) {
			if (Map[i][j] && Map[i][j + 1] && Map[i + 1][j] && Map[i + 1][j + 1]) {
				cnt++;
			}
		}
	}

	cout << cnt << endl;

	return 0;
}