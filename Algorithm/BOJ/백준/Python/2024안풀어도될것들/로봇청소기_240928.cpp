// https://www.acmicpc.net/problem/14503

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

int N, M;
int stRow, stCol;
int curD;
int ans = 0;
int dRow[] = {-1, 0, 1, 0}; // 북 동 남 서
int dCol[] = {0, 1, 0, -1};
vector<vector<int>> Map; // 1 : 벽 , 0은 빈칸, 2는 청소한 칸.

// 반시계 90도 회전
int rotate(int dir)
{
	switch (dir)
	{
	case 0 : return 3;
	case 1 : return 0;
	case 2 : return 1;
	case 3 : return 2;
	}
}

// 반대 방향
int opposite(int dir)
{
	switch (dir)
	{
		case 0 : return 2;
		case 1 : return 3;
		case 2 : return 0;
		case 3 : return 1;
	}
}

int checkEnableDir(int curRow, int curCol)
{
	for (int i = 0; i < 4; ++i)
	{
		int nxtRow = curRow + dRow[i];
		int nxtCol	= curCol + dCol[i];
		if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= M)
			continue;
		if (Map[nxtRow][nxtCol] == 0)
			return i;
	}
	return -1;
}

void Input()
{
	cin >> N >> M;
	Map.resize(N, vector<int>(M, 0));
	cin >> stRow >> stCol >> curD;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> Map[i][j];	
}

void Solve()
{
	int curRow = stRow, curCol = stCol;
	while (true)
	{
		// 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
		if (Map[curRow][curCol] == 0)
		{
			ans++;
			Map[curRow][curCol] = 2;
		}

		int enableDir = checkEnableDir(curRow, curCol);

		if (enableDir == -1) // 청소 가능한 구역 x
		{
			// 후진
			int oppDir = opposite(curD);
			int nxtRow = curRow + dRow[oppDir];
			int nxtCol = curCol + dCol[oppDir];
			// 후진 할 수 없는 경우, 다시 되돌아가기.
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= M)
				continue;
			// 벽이라면 동작을 멈춘다
			if (Map[nxtRow][nxtCol] == 1)
				break;
			curRow = nxtRow;
			curCol = nxtCol;
		}
		else
		{
			// 4방향 90도 회전
			for (int i = 0; i < 4; ++i)
			{
				curD = rotate(curD);

				int nxtRow = curRow + dRow[curD];
				int nxtCol = curCol + dCol[curD];
				if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= M)
					continue;
				if (Map[nxtRow][nxtCol] != 0)
					continue;
				// 해당 방향 전진
				curRow = nxtRow;
				curCol = nxtCol;
				break;
			}
		}
	}
	
	cout << ans << endl;
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


