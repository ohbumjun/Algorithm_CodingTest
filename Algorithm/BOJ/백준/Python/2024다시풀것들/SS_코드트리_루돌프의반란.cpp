// https://www.codetree.ai/training-field/frequent-problems/problems/rudolph-rebellion/description?page=2&pageSize=5

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
// #include <climits>
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

int N, M, P, C, D;
int ans = 0;

// 8 방향, 상우하좌, 대각선 (왼위, 오위, 왼아래, 오아래)
int dRow[] = {-1, 0, 1, 0, -1, -1, 1, 1};
int dCol[] = {0,  1, 0, -1, -1, 1, -1, 1};

vector<vector<int>> board;	// N * N
vector<bool> aliveSantas;	// 탈락 여부
vector<int> deadTime;		// 기절 시간 -> 0보다 크면, 기절 상태
int roudolfRow, roudolfCol;
vector<vector<int>> stataPosMap;	// N * N
vector<int> santaScores;

// 1. 어려웠던 것 : 상우좌하순
// 루돌프가 가장 가까운 산타 방향으로 돌진..?
// 2. 루돌프가 충돌하는 직후에 , 바로 산타가 날아가는 것.
// 산타가 모두 기다린 이후에 처리하는 것 아니다.
// 3. 하나의 턴에서 루돌프와 산타 충돌이 동시에 발생할 수 있다.

int optDir(int dir)
{
	if (dir == 0)
		return 2;
	else if (dir == 1)
		return 3;
	else if (dir == 2)
		return 0;
	else if (dir == 3)
		return 1;
}
void Input()
{
	cin >> N >> M >> P >> C >> D;

	board.resize(N, vector<int>(N, 0));
	stataPosMap.resize(N, vector<int>(N, -1));

	cin >> roudolfRow >> roudolfCol;
	roudolfRow -= 1;
	roudolfCol -= 1;

	santaScores.resize(P + 1, 0);
	deadTime.resize(P + 1, 0);
	aliveSantas.resize(P + 1, true);

	for (int p = 1; p <= P; ++p)
	{
		int pIdx, r, c;
		cin >> pIdx >> r >> c;
		stataPosMap[r - 1][c - 1] = pIdx;
	}
}

// move_santa 도 queue 형태로 처리해도 된다.
void moveSanta(int stR, int stC, int moveCnt, 
	int santa, int addedR, int addedC)
{
	// santa 를 stR, stC 에서 addR, addC 방향으로
	// moveCnt 칸 만큼 이동
	queue<tuple<int,int, int, int>> q;
	q.push({santa, stR, stC, moveCnt});

	while (!q.empty())
	{
		// q. 에 있는 녀석을
		int curRow, curCol, curSanta, move;
		tie(curRow, curCol, curSanta, move) = q.front();
		q.pop();

		int nxtRow = curRow + addedR * move;
		int nxtCol = curCol + addedC * move;

		// 범위를 벗어났다면, 탈락 처리
		if (nxtRow < 0 || nxtRow >= N ||
			nxtCol < 0 || nxtCol >= N)
		{
			aliveSantas[curSanta] = false;
			return;
		}
		else
		{
			// 범위 안
			if (stataPosMap[nxtRow][nxtCol] == -1)
			{
				// 2) 해당 위치에 기존 산타가 없었다면, 
				//	이동 처리만 하고 바로 나온다.
				stataPosMap[nxtRow][nxtCol] = curSanta;
				return;
			}
			else
			{
				// 1) 해당 위치에 기존 산타가 있었다면.
				//	queue 에 다시 넣는다.
				int oldSanta = stataPosMap[nxtRow][nxtCol];
				stataPosMap[nxtRow][nxtCol] = curSanta;
				q.push({ oldSanta, nxtRow, nxtCol, 1});
			}
		}
	}
}

void Solve()
{
	for (int turn = 0; turn < M; ++turn)
	{
		// 모든 산타 탈락이면 break.
		int aliveCnt = 0;
		for (int p = 1; p <= P; ++p)
			if (aliveSantas[p])
				aliveCnt += 1;

		// 1. 루돌프 이동
		// - 모든 산타 비교 => bfs (X), 그냥 산타 위치랑 일일히 비교
		// - 행큰, 열큰 정렬 (sort 함수 사용)
		// - 루돌프 방향도, bfs 가 아니라, 그냥 row, col 끼리만 비교.
		int rouDirR = 0, rouDirC = 0;
		int minDist = INT_MAX;
		vector<pair<int,int>> posToSantas;

		for (int r = 0; r < N; ++r)
		{
			for (int c = 0; c < N; ++c)
			{
				if (stataPosMap[r][c] == -1)
					continue;
				int dist = (r - roudolfRow) * (r - roudolfRow) 
					+ (c - roudolfCol) * (c - roudolfCol);
				if (dist < minDist)
				{
					minDist = dist;
					posToSantas.clear();
					posToSantas.push_back({ r, c });
				}
				else if (dist == minDist)
				{
					posToSantas.push_back({ r, c });
				}
			}
		}

		int closeStRow = posToSantas[posToSantas.size() - 1].first;
		int closeStCol = posToSantas[posToSantas.size() - 1].second;

		if (closeStRow > roudolfRow)
			rouDirR = 1;
		else if (closeStRow < roudolfRow)
			rouDirR = -1;

		if (closeStCol > roudolfCol)
			rouDirC = 1;
		else if (closeStCol < roudolfCol)
			rouDirC = -1;

		roudolfRow += rouDirR;
		roudolfCol += rouDirC;

		if (stataPosMap[roudolfRow][roudolfCol] != -1)
		{
			// - 충돌시 : move_santa(상호작용) => 이거를 나는 마지막에 했었음.
			//		- 점수 획득
			//		- 기절 처리.
			int collideSanta = stataPosMap[roudolfRow][roudolfCol];

			santaScores[collideSanta] += C;
			deadTime[collideSanta] += 2;

			// 기존 산타 위치 X
			stataPosMap[roudolfRow][roudolfCol] = -1;

			moveSanta(roudolfRow, roudolfCol, C, 
				collideSanta, rouDirR, rouDirC);
		}


		// 1. move santa
		// 2. dead time 처리 방식.


		// 2. 모든 산타 이동
		// - 기절, 탈락 제외
		// - 루돌프 가까워지는 방향
		//		- 다른 산타 X
		//		- 상,우,좌,하 순으로 (우선 순위 고려하는 방법 간단하다)
		//		- 경로는 어떻게 얻어옴 ? => 나는 BFS 에서 아예 배열로 함.
		//		- 마찬가지로 그냥 모든 경로 고려할 필요 X. 
		//			그냥 4방향 탐색 only

		for (int p = 1; p <= P; ++p)
		{
			if (aliveSantas[p] == false)
				continue;
			if (deadTime[p] > 0)
			{
				deadTime[p] -= 1;
				continue;
			}

			// board 를 뒤져서, 산타 위치를 찾는다
			int stRow = -1, stCol = -1;
			for (int r = 0; r < N; ++r)
			{
				for (int c = 0; c < N; ++c)
				{
					if (stataPosMap[r][c] == p)
					{
						stRow = r;
						stCol = c;
						break;
					}
				}
			}

			int minDist = (stRow - roudolfRow) *
				(stRow - roudolfRow)
				+ (stCol - roudolfCol) * 
				(stCol - roudolfCol);

			vector<int> santaNextDir;

			for (int d = 0; d < 4; ++d)
			{
				int nxtRow = stRow + dRow[d];
				int nxtCol = stCol + dCol[d];
				// 범위 out 고려 X
				if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
					continue;
				// 다른 산타 X
				if (stataPosMap[nxtRow][nxtCol] != -1)
					continue;
				int curDist = (nxtRow - roudolfRow) * 
					(nxtRow - roudolfRow) 
					+ (nxtCol - roudolfCol) * 
					(nxtCol - roudolfCol);
				if (curDist < minDist)
				{
					minDist = curDist;
					santaNextDir.push_back(d);
				}
			}

			if (santaNextDir.size() == 0)
				continue;

			// 맨 마지막
			int minDir = santaNextDir[santaNextDir.size() - 1];

			// 이동
			int movedRow = stRow + dRow[minDir];
			int movedCol = stCol + dCol[minDir];

			stataPosMap[stRow][stCol] = -1;

			// - 루돌프 충돌시 
			//	- 점수
			//	- 기절 처리
			//	- 상호 작용
			if (movedRow == roudolfRow && movedCol == roudolfCol)
			{
				santaScores[p] += D;
				deadTime[p] += 2;
				// 반대 방향
				int moveDir = optDir(minDir);
				int addedR = dRow[moveDir];
				int addedC = dCol[moveDir];
				moveSanta(movedRow, movedCol, D, p, 
					addedR, addedC);
			}
			else
			{
				// 충돌 X
				stataPosMap[movedRow][movedCol] = p;
			}
		}

		// 3. alive 인 경우 점수 + 1
		for (int p = 1; p <= P; ++p)
		{
			if (aliveSantas[p] == false)
				continue;
			santaScores[p] += 1;
		}
	}

	for (int p = 1; p <= P; ++p)
	{
		cout << santaScores[p] << " ";
	}
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


