// https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description?page=4&pageSize=5

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

// n : 격자크기
// m : 팀 개수
// k : 라운드 수
int N, M, K;

// 초기 Board (변하는 정보)
vector<vector<int>> Board; 

// 각 칸이 몇번째 그룹에 속하는 가. (변하지 않는 정보)
vector<vector<int>> Group;

// 각 그룹 점수
vector<int> Score;

vector<vector<pair<int, int>>> GroupCans;

// 4방향
int dRow[] = { 0, -1, 0, 1 };
int dCol[] = { 1, 0, -1, 0 };

int getOptDir(int cDir)
{
	if (cDir == 0)
		return 2;
	if (cDir == 1)
		return 3;
	if (cDir == 2)
		return 0;
	if (cDir == 3)
		return 1;
}

vector<pair<int, int>> dfs(int stR, int stC, vector<vector<bool>>& tempCheck)
{
	// 0 이 아닌 칸이면 계속 이동한다.
	// 이동선 각 칸은, 2개의 인접칸 만이 존재한다고 했다.
	// 따라서, 인접한 다른 팀의 이동칸은 없다고 가정한다.
	vector<pair<int, int>> moveCans;

	// row, col, dir, moveCans
	queue<tuple<int, int, int, vector<pair<int,int>>>> q;
	moveCans.push_back({ stR, stC });
	q.push({ stR, stC, -1, moveCans });

	while (!q.empty())
	{
		int curR, curC, curD;
		vector<pair<int,int>> curMoveCans;
		tie(curR, curC, curD, curMoveCans) = q.front();
		q.pop();

		tempCheck[curR][curC] = true;

		int opDir = -1;
		if (curD != -1)
		{
			opDir = getOptDir(curD);

			// 다시 되돌아온 것
			if (curR == stR && curC == stC)
			{
				curMoveCans.pop_back(); // 마지막 원소는 시작 r,c 와 동일할 것이다.
				return curMoveCans;
			}
		}

		for (int d = 0; d < 4; ++d)
		{
			int nxtRow = curR + dRow[d];
			int nxtCol = curC + dCol[d];
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
				continue;
			if (Board[nxtRow][nxtCol] <= 0)
				continue;
			if (opDir != -1 && opDir == d)
				continue;

			curMoveCans.push_back({ nxtRow, nxtCol });
			q.push({ nxtRow, nxtCol, d, curMoveCans });
			curMoveCans.pop_back();

			// 한방향으로만 이동
			break;
		}
	}

	return moveCans;
}

void Input()
{
	cin >> N >> M >> K;

	Board.resize(N, vector<int>(N, -1));
	Group.resize(N, vector<int>(N, -1));
	Score.resize(N, 0);

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < N; ++c)
			cin >> Board[r][c];

	// 그룹을 만들기 위한 check 배열
	vector<vector<bool>> tempCheck(N, vector<bool>(N, false));
	
	int groupCnt = 0;

	for (int r = 0; r < N; ++r)
	{
		for (int c = 0; c < N; ++c)
		{
			// 0 보다 클 경우, dfs 로 이동선 정보를 탐색한다.
			if (Board[r][c] == 0)
				continue;

			if (tempCheck[r][c])
				continue;

			// 굳이 모아둘 필요가 있을까 ?
			// 그냥 몇번째 집단 ? 인지만 알면 되는 것 아닌가 ?
			// 어떤 애들끼리 같은 집단에 속해있는지만 알면 되는 것 아닌가 ?

			// 머리 이동
			// 그리고 이동할 때는, 그냥 주변 4방향
			// 0 이 아니고, 그리고 2도 아닌 방향으로 이동하면 되는거 아닌가 ?
			// 아니면, 모든 것은, "꼬리" 를 기준으로 하면 된다.
			// 결국 "꼬리" to "2" 방향이 이동 방향이 되는 것이니까
			// 이동은 dfs ? 같이 처리하면 될 것 같고
			// 아니면 queue 로. 그저 이전 방향으로만 움직이지 않으면 되는 거니까.

			// 이동선 모음
			vector<pair<int, int>> moveCans = dfs(r, c, tempCheck);

			for (const pair<int, int>& posInfo : moveCans)
				Group[posInfo.first][posInfo.second] = groupCnt;

			groupCnt += 1;
			
			// // 0 : 빈칸
			// // 1 : 머리사람
			// // 2 : 나머지
			// // 3 : 꼬리사람
			// // 4 : 이동선
			GroupCans.push_back(moveCans);
		}
	}
}

int getKIndex(int initRow, int initCol)
{
	int groupN = Group[initRow][initCol];

	// 이동선을 조사해서, 머리를 찾는다
	int headIdx = -1;
	
	const vector<pair<int,int>>& groupCans = GroupCans[groupN];

	for (int i = 0; i < groupCans.size(); ++i)
	{
		const pair<int, int>& posInfo = groupCans[i];
		if (Board[posInfo.first][posInfo.second] == 1)
		{
			headIdx = i;
			break;
		}
	}

	int headRow = groupCans[headIdx].first;
	int headCol = groupCans[headIdx].second;

	// d, k, r, c
	queue<tuple<int, int, int, int>> q;
	q.push({ -1, 1, headRow, headCol });

	while (!q.empty())
	{
		// 4가 아닌 방향으로만 계속 가면 된다. 
		int curD, curK, curR, curC;
		tie(curD, curK, curR, curC) = q.front();
		q.pop();

		if (curR == initRow && curC == initCol)
		{
			return curK;
		}

		for (int d = 0; d < 4; ++d)
		{
			int nxtRow = curR + dRow[d];
			int nxtCol = curC + dCol[d];
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
				continue;
			if (Board[nxtRow][nxtCol] == 0 || Board[nxtRow][nxtCol] == 4)
				continue;
			// 머리, 꼬리가 붙어있는 경우도 있을 수 있다.
			// 이 경우는 꼬리도 X
			if (headRow == curR && headCol == curC)
			{
				if (Board[nxtRow][nxtCol] == 3)
					continue;	
			}
			if (curD != -1)
			{
				int optDir = getOptDir(curD);
				// 이전 방향으로 X
				if (optDir == d)
					continue;
			}
			q.push({ d, curK + 1, nxtRow, nxtCol });
		}
	}
}

void changeHeadTail(int group)
{
	int tailIdx = -1;
	int headIdx = -1;

	vector<pair<int, int>>& groupCans = GroupCans[group];

	for (int i = 0; i < groupCans.size(); ++i)
	{
		int row = groupCans[i].first;
		int col = groupCans[i].second;

		// tail
		if (Board[row][col] == 3)
		{
			tailIdx = i;
		}
		// head
		else if (Board[row][col] == 1)
		{
			headIdx = i;
		}
	}

	pair<int,int>& headPos = groupCans[headIdx];
	pair<int,int>& tailPos = groupCans[tailIdx];

	Board[headPos.first][headPos.second] = 3;
	Board[tailPos.first][tailPos.second] = 1;
}

void moveGroup(int groupN)
{
	// 이동선을 조사해서, "꼬리"를 찾는다.
	int tailIdx = -1;
	int headIdx = -1;

	// 새롭게 세팅되는 Board 정보
	// - 앞에서부터 차례대로 세팅하면 된다.
	vector<tuple<int, int, int>> newMoveInfos;
	newMoveInfos.reserve(N * N);

	const vector<pair<int, int>>& groupCans = GroupCans[groupN];

	for (int i = 0; i < groupCans.size(); ++i)
	{
		const pair<int, int>& posInfo = groupCans[i];
		if (Board[posInfo.first][posInfo.second] == 3)
			tailIdx = i;
		if (Board[posInfo.first][posInfo.second] == 1)
			headIdx = i;
	}

	int tailRow = groupCans[tailIdx].first;
	int tailCol = groupCans[tailIdx].second;

	int headRow = groupCans[headIdx].first;
	int headCol = groupCans[headIdx].second;

	// newMoveInfos.push_back({ 4, tailRow, tailCol });

	// d, newV, prevV, r, c
	queue<tuple<int, int, int, int, int>> q;
	q.push({ -1, 4, 3, tailRow, tailCol }); // 꼬리는 4 로 만든다. (일반 이동칸)

	while (!q.empty())
	{
		// 4가 아닌 방향으로만 계속 가면 된다. 
		int curD, newV, prevV, curR, curC;
		tie(curD, newV, prevV, curR, curC) = q.front();
		q.pop();

		newMoveInfos.push_back({ newV, curR, curC });

		for (int d = 0; d < 4; ++d)
		{
			int nxtRow = curR + dRow[d];
			int nxtCol = curC + dCol[d];
			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
				continue;
			if (Board[nxtRow][nxtCol] == 0)
				continue;
			if (curR == headRow && curC == headCol)
			{
				// 단, "기준" 이 머리의 경우에는 앞에 가는 경로에 "이동칸" 이 있을 수 있다.
				bool isHead = true;
			}
			else
			{
				// 자. 머리를 제외하고는 가려고 하는 경로에 4가 있을 경우 이동 X
				if (Board[nxtRow][nxtCol] == 4)
					continue;
			}

			// 머리, 꼬리가 붙어있는 경우도 있을 수 있다.
			// 이 경우는 머리도 X
			if (tailRow == curR && tailCol == curC)
			{
				if (Board[nxtRow][nxtCol] == 1)
					continue;
			}
			if (curD != -1)
			{
				int optDir = getOptDir(curD);
				// 이전 방향으로 X
				if (optDir == d)
					continue;
			}

			int curValue = Board[nxtRow][nxtCol];

			// 그 다음에서는, nxtRow, nxtCol 에 prevV 을 세팅한다.
			// 즉, prevV 을 newV 형태로 넘겨주면 된다.
			// 그리고 현재값을 prevV 로 넘겨준다.
			q.push({ d, prevV, curValue, nxtRow, nxtCol });
		}
	}

	for (int i = 0; i < newMoveInfos.size(); ++i)
	{
		int value, row, col;
		tie(value, row, col) = newMoveInfos[i];
		Board[row][col] = value;
	}
}

void Solve()
{
	/*
	* N * N 격자
	* - 3명 이상 한 팀
	* - 맨 앞 : 머리 사람/ 맨 뒤 : 꼬리 사람
	* - 게임에서 "주어진 선으로만" 이동
	* - 각 팀 이동선은, 재귀 (끝이 이어짐)
	* - 각 팀 이동선 겹침 X
	*/

	/*
	* 라운드 진행
	* 1) 머리사람을 따라 각 팀 이동
	* 2) 상하좌우에서, 공이 날아온다.
	* - 이때 각 라운드별로, 날아오는 방향이 정해져 있다.
	* - 4n 부터는 다시 원점
	* 3) 최초 공 맞은 사람"만" 공, 점수 획득
	* - 얻는 점수 : "머리사람" 기준 k 번째 ^ 2 (1부터)
	* - 아무도 점수 획득 못할 경우, 아무런 처리 X
	* - 공획득한 팀 => 머리사람. 꼬리 사람 바뀜 (방향 변경)
	*/

	/*
	* >> 상태
	* 
	* 0 : 빈칸
	* 1 : 머리사람
	* 2 : 나머지
	* 3 : 꼬리사람
	* 4 : 이동선
	*/

	// for (int r = 0; r < 4 * N; ++r)
	for (int r = 0; r < K; ++r)
	{
		int d, stR, stC;
		
		// 각 팀 이동
		for (int grp = 0; grp < GroupCans.size(); ++grp)
			moveGroup(grp);
		
		// 라인 쏘기
		// 시작 라인을 미리 정해두는 것이 아니라, 그때그때 구하는 방법 ?
		// tie(d, stR, stC) = Lines[r];

		int divd = r / N;
		int rest = r % N;
		d = divd;

		if (divd == 0) // 위에서 아래로
		{
			// ex) N : 7, r = 6
			stR = rest;
			stC = 0;
		}
		else if (divd == 1) // 왼쪽에서 오른쪽
		{
			// ex) N : 7, r = 7
			// int stRow = N - 1;
			// int stCol = n;
			stR = N - 1;
			stC = rest;
		}
		else if (divd == 2) // 아래에서 위로
		{
			// int stRow = n;
			// int stCol = N - 1;
			// ex) N : 7, r = 14, div : 2, rest : 0
			// ex) N : 7, r = 15, div : 2, rest : 1
			stR = N - 1 - rest;
			stC = N - 1;
		}
		else  if (divd == 3) // 오른쪽에서 왼쪽
		{
			// ex) N : 7, r = 22, div : 3, rest : 1
			// int stRow = 0;
			// int stCol = n;
			stR = 0;
			stC = N - 1 - rest;
		}

		for (int n = 0; n < N; ++n)
		{
			int curRow = stR + dRow[d] * n;
			int curCol = stC + dCol[d] * n;

			// 해당 위치에 부딪힐 대상이 있는지 확인한다.
			if (Board[curRow][curCol] == 0 || Board[curRow][curCol] == 4)
				continue;

			// 최초 부딪힌 대상에 대한 처리
			int GroupNum = Group[curRow][curCol];

			int k = getKIndex(curRow, curCol);

			Score[GroupNum] += k * k;

			// 머리, 꼬리 변경
			changeHeadTail(GroupNum);

			break;
		}
	}

	// 각 팀이 획득한 점수의 총합
	int ans = 0;
	for (int g = 0; g < GroupCans.size(); ++g)
		ans += Score[g];
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


