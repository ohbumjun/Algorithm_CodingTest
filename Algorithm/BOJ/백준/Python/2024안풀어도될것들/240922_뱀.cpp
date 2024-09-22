// https://www.acmicpc.net/problem/3190

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

int N, K, L;
vector<vector<int>> board;		// 1 : 사과 , out : 벽
vector<vector<bool>> self;		// 자기 자신이 위치한 위치 정보
vector<vector<char>> dirMap;		// 해당 위치에서 변해야할 정보
unordered_map<int, char> dirInfo;	// 시간, 방향 정보
int dRow[4] = { 0, 1, 0, -1 };		// 오, 아, 왼, 위
int dCol[4] = { 1, 0, -1, 0 };

int changeDir(int cDir, char c)
{
	// 왼쪽 90도
	if (c == 'L')
	{
		switch (cDir)
		{
		case 0 :
			return 3;
		case 1 :
			return 0;
		case 2 :
			return 1;
		case 3 :
			return 2;
		}
	}
	else // 'D' 오른쪽 90도
	{
		switch (cDir)
		{
		case 0:
			return 1;
		case 1:
			return 2;
		case 2:
			return 3;
		case 3:
			return 0;
		}
	}
}

void debugSelf()
{
	cout << "Self" << endl;
	for (int r = 0; r < N; ++r)
		{
			for (int c = 0; c < N; ++c)
			{
			cout << self[r][c] << " ";
		}
		cout << endl;
	}
	cout << "----" << endl;
}

void Input()
{
	cin >> N;
	cin >> K;

	board.resize(N, vector<int>(N, 0));
	self.resize(N, vector<bool>(N, false));
	dirMap.resize(N, vector<char>(N, ' '));

	for (int k = 0; k < K; ++k)
	{
		int x, y;
		cin >> x >> y;
		board[x - 1][y - 1] = 1;
	}

	cin >> L;

	for (int l = 0; l < L; ++l)
	{
		int x;
		char c;
		cin >> x >> c;
		dirInfo[x] = c;
	}
}

void Solve()
{
	int cTime = 0;
	int cHeadRow = 0, cHeadCol = 0;
	int cDir = 0;
	vector<pair<int, int>> snakes;
	vector<int> snakeDir;

	snakes.push_back({ cHeadRow, cHeadCol });
	snakeDir.push_back(cDir);

	self[cHeadRow][cHeadCol] = true;

	while (true)
	{
		if (dirInfo.find(cTime) != dirInfo.end())
		{
			// cout << "change" << endl;
			cDir = changeDir(cDir, dirInfo[cTime]);
			dirMap[cHeadRow][cHeadCol] = dirInfo[cTime];
		}
		else
		{
			// 그런데 현재 dirMap 에 저장된 값이 존재한다면 reset
			if (dirMap[cHeadRow][cHeadCol] != ' ')
			{
				dirMap[cHeadRow][cHeadCol] = ' ';
			}
		}

		int nxtRow = cHeadRow + dRow[cDir];
		int nxtCol = cHeadCol + dCol[cDir];

		// 벽. 혹은 자기 자신이면 종료
		bool isWall = nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N;

		if (isWall || self[nxtRow][nxtCol])
			break;

		bool isApple = board[nxtRow][nxtCol] == 1;

		int lastRow = snakes.back().first;
		int lastCol = snakes.back().second;

		// 일단 모든 몸통을 한칸씩 이동
		// 단, head 는 새로운 방향이라면 새로운 방향으로
		// 그외는 기존 방향대로
		int lastBodyDir = snakeDir.back();
		for (int i = 0; i < snakes.size(); ++i)
		{
			int mDir = snakeDir[i];

			pair<int, int>& s = snakes[i];

			// 이전 위치 false
			self[s.first][s.second] = false;

			if (dirMap[s.first][s.second] != ' ')
			{
				mDir = changeDir(mDir, dirMap[s.first][s.second]);
				snakeDir[i] = mDir;
			}

			// 이동
			s.first += dRow[mDir];
			s.second += dCol[mDir];
			self[s.first][s.second] = true;
		}

		if (isApple)
		{
			snakes.push_back({ lastRow, lastCol });

			snakeDir.push_back(lastBodyDir);

			self[lastRow][lastCol] = true;

			// 사과 먹기
			board[nxtRow][nxtCol] = 0;
		}
		
		cHeadRow = nxtRow;
		cHeadCol = nxtCol;

		cTime += 1;

		// cout << "cTime : " << cTime << endl;
		// debugSelf();
	}

	cout << cTime + 1 << endl;
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
