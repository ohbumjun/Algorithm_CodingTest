// https://www.acmicpc.net/problem/19238

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
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

// N : 행,열
// M : 상어 수
int N, M;
int stRow, stCol, stFuel;
vector<vector<int>> Map;
vector<pair<int,int>> stPos;
vector<pair<int,int>> edPos;
vector<bool> arrived;
int dRow[] = { -1, 1, 0, 0 };
int dCol[] = { 0, 0, -1, 1 };


void Input()
{
	cin >> N >> M >> stFuel;

	stPos.resize(M);
	edPos.resize(M);
	arrived.resize(M, false);

	Map.resize(N, vector<int>(N, 0));

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> Map[i][j];

	cin >> stRow >> stCol;
	stRow -= 1;
	stCol -= 1;

	for (int m = 0; m < M; ++m)
	{
		int stR, stC, edR, edC;
		cin >> stR >> stC >> edR >> edC;
		stPos[m] = { stR - 1, stC - 1 };
		edPos[m] = { edR - 1, edC - 1 };
	}
}

pair<int, int> findNear(int taxiR, int taxiC)
{
	// 승객 거리
	vector<vector<bool>> check;
	vector<vector<int>> dist;
	check.resize(N, vector<bool>(N, false));
	dist.resize(N, vector<int>(N, INT_MAX));
	
	queue<tuple<int, int, int>> q;
	q.push({ taxiR, taxiC, 0 });
	dist[taxiR][taxiC] = 0;
	check[taxiR][taxiC] = true;

	while (!q.empty())
	{
		int curR, curC, curDist;
		tie(curR, curC, curDist) = q.front();
		q.pop();

		for (int d = 0; d < 4; ++d)
		{
			int nxtRow = curR + dRow[d];
			int nxtCol = curC + dCol[d];

			// 격자 밖
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
				continue;

			// 벽
			if (Map[nxtRow][nxtCol] == 1)
				continue;

			// 이미 방문
			if (check[nxtRow][nxtCol])
				continue;

			// 거리 갱신
			check[nxtRow][nxtCol] = true;
			dist[nxtRow][nxtCol] = min(dist[nxtRow][nxtCol], curDist + 1);
			q.push({ nxtRow, nxtCol, curDist + 1 });
		}
	}

	int minClient = -1;
	int minDist = INT_MAX;

	for (int client = 0; client < M; ++client)
	{
		if (arrived[client])
			continue;
		
		int curClientRow = stPos[client].first;
		int curClientCol = stPos[client].second;
		int distToClient = dist[curClientRow][curClientCol];

		if (distToClient == INT_MAX) // 해당 칸으로 갈 수 없다면
			continue;

		if (distToClient > minDist)
			continue;

		// 현재 택시 위치에서 최단 거리 승객을 채운다.
		// - 여러 명이면, "행" 이 가장 작은 승객
		// - "행" 이 같으면, "열" 이 가장 작은 승객
		// - 택시, 승객 같은 곳에 있으면 최단 거리 0
		if (distToClient == minDist)
		{
			int minClientRow = stPos[minClient].first;
			int minClientCol = stPos[minClient].second;

			if (minClientRow > curClientRow)
			{
				minClient = client;
				minDist = distToClient;
			}
			else if (minClientRow == curClientRow)
			{
				if (minClientCol > curClientCol)
				{
					minClient = client;
					minDist = distToClient;
				}
			}
		}
		else if (distToClient < minDist)
		{
			minClient = client;
			minDist = distToClient;
		}
	}

	return { minClient, minDist };
}

int findDistEnd(int client)
{
	// 승객 거리
	int clientStRow = stPos[client].first;
	int clientStCol = stPos[client].second;

	vector<vector<bool>> check;
	vector<vector<int>> dist;
	check.resize(N, vector<bool>(N, false));
	dist.resize(N, vector<int>(N, INT_MAX));

	queue<tuple<int, int, int>> q;
	q.push({ clientStRow, clientStCol, 0 });
	dist[clientStRow][clientStCol] = 0;
	check[clientStRow][clientStCol] = true;

	while (!q.empty())
	{
		int curR, curC, curDist;
		tie(curR, curC, curDist) = q.front();
		q.pop();

		for (int d = 0; d < 4; ++d)
		{
			int nxtRow = curR + dRow[d];
			int nxtCol = curC + dCol[d];

			// 격자 밖
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
				continue;

			// 벽
			if (Map[nxtRow][nxtCol] == 1)
				continue;

			// 이미 방문
			if (check[nxtRow][nxtCol])
				continue;

			// 거리 갱신
			check[nxtRow][nxtCol] = true;
			dist[nxtRow][nxtCol] = min(dist[nxtRow][nxtCol], curDist + 1);
			q.push({ nxtRow, nxtCol, curDist + 1 });
		}
	}

	int targetRow = edPos[client].first;
	int targetCol = edPos[client].second;
	return dist[targetRow][targetCol];
}

void Solve()
{
	// 승객 내려줄 때마다, 연료 충전
	// 연로 바닥나면 업무 종료

	// M 명 승객 태우기
	// 택시 빈칸 -> 상하좌우 중 인접칸 이동 가능
	// 승객은 빈칸에. 다른 빈칸으로 이동하려고 한다.
	// 여러 승객 같이 탑승 X
	// 한 승객 태워서, 목적지까지 이동시켜야 함
	// 승객은, 스스로 움직이지 X
	// 출발지에서만 택시타고, 목적지에서만 택시 내림



	int movedCnt = 0;
	int curFuel = stFuel;
	int curTaxiRow = stRow;
	int curTaxiCol = stCol;

	while (curFuel > 0)
	{
		if (movedCnt == M)
			break;
		pair<int,int> nxtClientInfo = findNear(curTaxiRow, curTaxiCol);
		int nxtClient = nxtClientInfo.first;
		int distToClient = nxtClientInfo.second;

		// - 연료는 1칸 이동 할 때마다 1 소모
		// - 목적지로 승객 이동시키면, 이동시키며 소모된 연료 2배 충전
		// - 이동 중 연로 바닥나면 X
		// 단, 승객을 목적지로 이동시킨 동시에, 연료 바닥나는 것은 ok
		curFuel -= distToClient;
		if (curFuel < 0)
			break;

		int distToEnd = findDistEnd(nxtClient);

		curFuel -= distToEnd;
		if (curFuel < 0)
			break;
		movedCnt += 1;
		curFuel += 2 * distToEnd;
		// 도착시키면, 해당 승객 정보 모두 지워줘야 한다
		arrived[nxtClient] = true;

		int edRow = edPos[nxtClient].first;
		int edCol = edPos[nxtClient].second;

		curTaxiRow = edRow;
		curTaxiCol = edCol;
	}

	if (movedCnt < M)
		cout << -1 << endl;
	else 
		cout << curFuel << endl;
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


