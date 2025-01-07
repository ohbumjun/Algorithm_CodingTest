// https://www.acmicpc.net/problem/14499

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

int N, M; // N : 행, M : 열
int dx, dy;
int K;
vector<vector<int>> map;
vector<int> command;
int dice[] = {0,0,0,0,0,0}; // 위,아래, 동, 서, 남, 북

// 동 서 북 남
int dirRow[] = { 0, 0, -1, 1 };
int dirCol[] = { 1, -1, 0, 0 };

void changeDice(int dir)
{
	int temp[6] = { 0, };

	// prev dice 출력
#ifdef DEBUG
	cout << "prev dice : " << endl;
	for (int i = 0; i < 6; ++i)
		cout << dice[i] << " ";
	cout << endl;

#endif // DEBUG

	for (int i = 0; i < 6; ++i)
	{
		temp[i] = dice[i];
	}

	switch (dir)
	{
	case 1: // 동 (오른쪽 굴림)
		dice[0] = temp[3]; // 서 -> 위
		dice[1] = temp[2]; // 동 -> 아래
		dice[2] = temp[0]; // 위 -> 동
		dice[3] = temp[1]; // 아래 -> 서
		dice[4] = temp[4]; // 남 -> 남
		dice[5] = temp[5]; // 북 -> 북
		break;
	case 2: // 서 (왼쪽 굴림)
		dice[0] = temp[2]; // 동 -> 위
		dice[1] = temp[3]; // 서 -> 아래
		dice[2] = temp[1]; // 아래 -> 동
		dice[3] = temp[0]; // 위 -> 서
		dice[4] = temp[4]; // 남 -> 남
		dice[5] = temp[5]; // 북 -> 북
		break;
	case 3: // 북
		dice[0] = temp[4]; // 남 -> 위
		dice[1] = temp[5]; // 북 -> 아래
		dice[2] = temp[2]; // 동 -> 동
		dice[3] = temp[3]; // 서 -> 서
		dice[4] = temp[1]; // 아래 -> 남
		dice[5] = temp[0]; // 위 -> 북
		break;
	case 4: // 남
		dice[0] = temp[5]; // 북 -> 위
		dice[1] = temp[4]; // 남 -> 아래
		dice[2] = temp[2]; // 동 -> 동
		dice[3] = temp[3]; // 서 -> 서
		dice[4] = temp[0]; // 위 -> 남
		dice[5] = temp[1]; // 아래 -> 북
		break;
	}

#ifdef DEBUG
	// aft dice 출력
	cout << "aft dice : " << endl;
	for (int i = 0; i < 6; ++i)
		cout << dice[i] << " ";
	cout << endl;
	cout << "---" << endl;
#endif // DEBUG
}

void Input()
{
	cin >> N >> M >> dx >> dy >> K;

	// 맨 처음 
	map.resize(N, vector<int>(M, 0));

	for (int n = 0; n < N; ++n)
		for (int m = 0; m < M; ++m)
			cin >> map[n][m];

	command.resize(K, 0);
	for (int k = 0; k < K; ++k)
		cin >> command[k];
}

void Solve()
{
	int diceRow = dx;
	int diceCol = dy;

	for (int k = 0; k < K; ++k)
	{
		int curCommand = command[k];

		// 이동
		int nextRow = diceRow + dirRow[curCommand - 1];
		int nextCol = diceCol + dirCol[curCommand - 1];

		// cout << "nextRow : " << nextRow << " nextCol : " << nextCol << endl;

		// 밖이면 무시 및 출력 X
		bool isOut = nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= M;

		if (isOut)
			continue;

		int mapValue = map[nextRow][nextCol];

		// cout << "mapValue : " << mapValue << endl;

		// 주사위 굴림
		changeDice(curCommand);

		if (mapValue == 0)
		{
			// 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨
			map[nextRow][nextCol] = dice[1];
		}
		else
		{
			// 지도에 있는 값이 주사위 바닥면으로 복사
			dice[1] = mapValue;

			// 해당 위치 0
			map[nextRow][nextCol] = 0;
		}

		// 주사위 윗면 출력
		cout << dice[0] << endl;

		// 주사위 모두 출력 (위, 아래, 동, 서, 남, 북)

#ifdef DEBUG
		// for (int i = 0; i < 6; ++i)
		// 	cout << dice[i] << " ";
		// cout << endl;
#endif // DEBUG

		diceRow = nextRow;
		diceCol = nextCol;
		// 
	}
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
