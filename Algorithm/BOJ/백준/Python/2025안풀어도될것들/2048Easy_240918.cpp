// https://www.acmicpc.net/problem/12100

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
vector<vector<int>> board;
int answer = INT_MIN;
int dRow[] = { 0, 0, 1, -1 }; // 오, 왼, 아, 위
int dCol[] = { 1, -1, 0, 0 };

void debug(vector<vector<int>>& curBoard, int dir)
{
	cout << "dir: " << dir << endl;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cout << curBoard[i][j] << " ";
		cout << endl;
	}
	cout << endl;
}

int getMaxValue(const vector<vector<int>>& curBoard)
{
	int ret = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			ret = max(ret, curBoard[i][j]);
	return ret;
}

void moveToEnd(vector<vector<int>>& curBoard, int dir)
{
	switch (dir)
	{
	case 0:	// 오
	{
		for (int r = 0; r < N; ++r)
		{
			// 오른쪽에서 왼쪽으로 가면서 끌어당기는 느낌
			int cIdx = N - 1;
			int lastSpot = -1;

			while (cIdx >= 0)
			{
				if (curBoard[r][cIdx] == 0)
				{
					if (lastSpot == -1)
						lastSpot = cIdx;
					cIdx--;
				}
				else
				{
					if (lastSpot == -1)
					{
						cIdx--;
						continue;
					}
					else
					{
						curBoard[r][lastSpot] = curBoard[r][cIdx];
						curBoard[r][cIdx] = 0;
						cIdx = lastSpot - 1;
						lastSpot = -1;
					}
				}
			}
		}
	}
	break;
	case 1: // 왼쪽으로 이동
	{
		for (int r = 0; r < N; ++r)
		{
			// 왼쪽에서 오른쪽으로 가면서 끌어당기는 느낌
			int cIdx = 0;
			int lastSpot = -1;

			while (cIdx < N)
			{
				if (curBoard[r][cIdx] == 0)
				{
					if (lastSpot == -1)
						lastSpot = cIdx;
					cIdx++;
				}
				else
				{
					if (lastSpot == -1)
					{
						cIdx++;
						continue;
					}
					else
					{
						curBoard[r][lastSpot] = curBoard[r][cIdx];
						curBoard[r][cIdx] = 0;
						cIdx = lastSpot + 1;
						lastSpot = -1;
					}
				}
			}
		}
	}
	break;
	case 2: // 아
	{
		for (int c = 0; c < N; ++c)
		{
			// 아래에서 계속 위로 올라가면서 끌어당기는 느낌
			int cIdx			= N - 1;
			int lastSpot = -1;

			while (cIdx >= 0)
			{
				if (curBoard[cIdx][c] == 0)
				{
					if (lastSpot == -1)
						lastSpot = cIdx;
					cIdx--;
				}
				else
				{
					if (lastSpot == -1)
					{
						cIdx--;
						continue;
					}
					else
					{
						curBoard[lastSpot][c] = curBoard[cIdx][c];
						curBoard[cIdx][c] = 0;
						cIdx = lastSpot - 1;
						lastSpot = -1;
					}
				}
			}
		}
	}
	break;
	case 3: // 위
	{
		for (int c = 0; c < N; ++c)
		{
			// 위에서 아래로 내려가면서 끌어당기는 느낌
			int cIdx = 0;
			int lastSpot = -1;

			while (cIdx < N)
			{
				if (curBoard[cIdx][c] == 0)
				{
					if (lastSpot == -1)
						lastSpot = cIdx;
					cIdx++;
				}
				else
				{
					if (lastSpot == -1)
					{
						cIdx++;
						continue;
					}
					else
					{
						curBoard[lastSpot][c] = curBoard[cIdx][c];
						curBoard[cIdx][c] = 0;
						cIdx = lastSpot + 1;
						lastSpot = -1;
					}
				}
			}
		}
	}
	break;
	}
}

void calculateMove(vector<vector<int>>& curBoard, int dir)
{
	// cout << "calculateMove: " << endl;
	// debug(curBoard, dir);

	switch (dir)
	{
		case 0:	// 오
			for (int r = 0; r < N; ++r)
			{
				// 오른쪽에서 왼쪽으로 
				int cIdx = N - 1;

				while (cIdx > 0)
				{
					// 현재 위치와, 왼쪽 위치를 비교한다.
					int nIdx = cIdx - 1;

					int cValue = curBoard[r][cIdx];
					int nValue = curBoard[r][nIdx];

					if (cValue == nValue)
					{
						// 만약 같다면, 하나로 합치고, cIdx 는 현재 칸 유지
						curBoard[r][cIdx] = cValue + nValue;

						// 그리고 왼쪽에 있는 모든 애들을 한칸식 이동시킨다.
						for (int i = nIdx; i > 0; --i)
						{
							curBoard[r][i] = curBoard[r][i - 1];
						}

						// 마지막 부분은 0으로 만들어줘야 한다.
						curBoard[r][0] = 0;
					}
					// 만약 같지 않다면 cIdx 한칸 이동
					cIdx--;
				}
			}
			break;
		case 1:	// 왼
			for (int r = 0; r < N; ++r)
			{
				// 왼쪽에서 오른쪽으로 
				int cIdx = 0;

				while (cIdx < N - 1)
				{
					// 현재 위치와, 오른쪽 위치를 비교한다.
					int nIdx = cIdx + 1;

					int cValue = curBoard[r][cIdx];
					int nValue = curBoard[r][nIdx];

					if (cValue == nValue)
					{
						// 만약 같다면, 하나로 합치고, cIdx 는 현재 칸 유지
						curBoard[r][cIdx] = cValue + nValue;

						// 그리고 오른쪽에 있는 모든 애들을 한칸식 이동시킨다.
						for (int i = nIdx; i < N - 1; ++i)
						{
							curBoard[r][i] = curBoard[r][i + 1];
						}

						curBoard[r][N - 1] = 0;
					}
					// 만약 같지 않다면 cIdx 한칸 이동
					cIdx++;
				}
			}
			break;
		case 2:	// 아
			for (int c = 0; c < N; ++c)
			{
				// 위에서 아래로 조사하면서 진행하기
				int rIdx = N - 1;

				while (rIdx > 0)
				{
					// 현재 위치와, 위쪽 위치를 비교한다.
					int nIdx = rIdx - 1;

					int cValue = curBoard[rIdx][c];
					int nValue = curBoard[nIdx][c];

					if (cValue == nValue)
					{
						// 만약 같다면, 하나로 합치고, rIdx 는 현재 칸 유지
						curBoard[rIdx][c] = cValue + nValue;

						// 그리고 위쪽에 있는 모든 애들을 한칸식 이동시킨다.
						for (int i = nIdx; i > 0; --i)
						{
							curBoard[i][c] = curBoard[i - 1][c];
						}

						curBoard[0][c] = 0;
					}
					// 만약 같지 않다면 rIdx 한칸 이동
					rIdx--;
				}
			}
			break;
		case 3:	// 위
			for (int c = 0; c < N; ++c)
			{
				// 아래에서 위로 조사하면서 진행하기
				int rIdx = 0;

				while (rIdx < N - 1)
				{
					// 현재 위치와, 아래쪽 위치를 비교한다.
					int nIdx = rIdx + 1;

					int cValue = curBoard[rIdx][c];
					int nValue = curBoard[nIdx][c];

					if (cValue == nValue)
					{
						// 만약 같다면, 하나로 합치고, rIdx 는 현재 칸 유지
						curBoard[rIdx][c] = cValue + nValue;

						// 그리고 아래쪽에 있는 모든 애들을 한칸식 이동시킨다.
						for (int i = nIdx; i < N - 1; ++i)
						{
							curBoard[i][c] = curBoard[i + 1][c];
						}
						curBoard[N - 1][c] = 0;
					}
					// 만약 같지 않다면 rIdx 한칸 이동
					rIdx++;
				}
			}
			break;
	}
}

vector<vector<int>> moveBoard(vector<vector<int>>& curBoard, int dir)
{
	vector<vector<int>> newBoard(curBoard);

	moveToEnd(newBoard, dir);

	calculateMove(newBoard, dir);

	return newBoard;
}

void dfs(int cnt, vector<vector<int>>& curBoard)
{
	if (cnt == 5)
	{
		int value = getMaxValue(curBoard);
		answer = max(answer, value);
		return;
	}

	for (int dir = 0; dir < 4; ++dir)
	{
		vector<vector<int>> newBoard = moveBoard(curBoard, dir);
		dfs(cnt + 1, newBoard);
	}
}

void Input()
{
	cin >> N;

	board.resize(N, vector<int>(N, 0));

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> board[i][j];
}

void Solve()
{
	dfs(0, board);

	cout << answer << endl;
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
