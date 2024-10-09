// https://www.acmicpc.net/problem/17825

// 1번째 풀이 => 틀림 + 시간 초과
/*
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

// 1.주사위 게임판을 어떤 형태로 관리할 것이냐
// - 일단 1차원 배열로 외곽 정보 저장
// - 파란색 칸 10 -> 24 : 2행
// - 20 -> 24 : 3행
// - 30 -> 34 : 4행
// - 25 -> 40 : 5행
// - 40 -> 도착 : 6행
// - 파란색 칸 -> 이동할 행 위치 정보도 저장.
// 2.모든 경우의 수를 어떻게 조사 ?
// - dfs 로 . 각 주사위 마다 이동시킬 말 조합들을 모아두기
// - 10pack ?

// n
// 그 다음 이동할 칸
vector<vector<tuple<int,int,int>>> board;
vector<int> dices;
int ans = 0;

bool checkDuplication(const vector<pair<int, int>>& malPoses, 
	int curR, int curC, int malIdx)
{
	for (int i = 0; i < malPoses.size(); ++i)
	{
		if (i == malIdx)
			continue;
		if (malPoses[i].first == curR && malPoses[i].second == curC)
			return true;
	}

	return false;
}

int move(vector<int>& mals)
{
	int totScore = 0;

	// 이동 마침 여부
	vector<bool> malCheck(4,false);

	// 말들의 위치
	vector<pair<int, int>> malPoses;

	for (int i = 0; i < 4; ++i)
		malPoses.push_back({ 0, 0 });

	// 화살표 방향으로 이동
	// 파란색 칸에서 이동 시작시, 파란색 화살표
	// 이동 중간 혹은 빨간색이면, 빨간색 화살표
	// 도착칸 도착시, 무조건 이동 X

	// 10개 턴.
	// 1 ~ 5개 숫자
	// 도착칸에 있지 않은 말 하나를 골라서, 주사위 수 만큼 이동
	// 이동 마치는 칸에 다른 말 있으면, 그 말은 고를 수 X
	// 단, 마치는 칸이 도착칸이면 가능
	// 이동 마칠 때마다 칸에 적힌 수 점수에 추가


	for (int idx = 0; idx < 10; ++idx)
	{
		int mal = mals[idx];

		// 이동 마친 mal 은 이동 X
		if (malCheck[mal])
			continue;

		int dice = dices[idx];

		const pair<int, int>& curPos = malPoses[mal];

		int curR = curPos.first;
		int curC = curPos.second;

		int nxtR = curR;
		int nxtC = curC;

		// 이동시킨다.
		// 0 인 행일 때는, 
		// 1) 이동 중일 때는, 그냥 바로 다음 col 로 이동
		// 2) 이동 중이 아닐 때는, 무조건 nxtR, nxtC 로 이동
		// 그 이외 행들은, 파란색이 없으므로, 그냥 nxtR, nxtC 로 이동

		for (int d = 0; d < dice; ++d)
		{
			nxtR = curR;
			nxtC = curC;
			if (curR == 0)
			{
				if (d == 0) // 맨 처음 이동
				{
					nxtR = get<1>(board[curR][curC]);
					nxtC = get<2>(board[curR][curC]);
				}
				else // 이동 중
				{
					nxtC += 1;

					// 맨 마지막 범위를 넘었다는 것은, 40으로 가야 한다는 것
					if (nxtC >= board[0].size())
					{
						nxtR = 5;
						nxtC = 0;
					}
				}
			}
			else
			{
				nxtR = get<1>(board[curR][curC]);
				nxtC = get<2>(board[curR][curC]);
			}

			// 도착 칸 범위를 벗어난다면
			if (nxtR == 5 && nxtC >= 1)
			{
				// 이동 마침
				break;
			}

			curR = nxtR;
			curC = nxtC;
		}

		int boardScore = get<0>(board[curR][curC]);

		// 이동 마친 칸에 다른 말이 있는지 확인
		if (nxtR == 5 && nxtC >= 1)
		{
			// 이동 마친 칸이 도착칸이라면
			// - 이동 마침
			malCheck[mal] = true;
		}
		else
		{
			// 도착 칸이 아니라면
			bool dup = checkDuplication(malPoses, curR, curC, mal);
			
			if (!dup)
			{
				// - 다른 말 없으면 이동 후 점수 추가
				totScore += boardScore;
				malPoses[mal] = { curR, curC };
			}
			else
			{
				// - 다른 말 있으면 이동 X
			}
		}
	}

	if (totScore == 212)
	{
		bool h = true;
	}

	return totScore;
}

void dfs(int cnt, vector<int>& mals)
{
	if (cnt == 10)
	{
		// 이동
		int totScore = move(mals);
		ans = max(ans, totScore);
		return;
	}

	for (int i = 0; i < 4; ++i)
	{
		if (cnt == 1 && i == 1)
		{
			bool h = true;
		}
		mals.push_back(i);
		dfs(cnt + 1, mals);
		mals.pop_back();
	}
}

void Input()
{


	for (int i = 0; i < 10; ++i)
	{
		int d;
		cin >> d;
		dices.push_back(d);
	}

	board.resize(6, vector<tuple<int, int, int>>());

	// 1행
	for (int i = 0; i < 20; i += 1)
	{
		int n = i * 2;
		int nxtR = 0;
		int nxtC = i + 1;

		// 가장 마지막 칸
		if (i == 19)
		{
			nxtR = 5; // 5,0 에는 40이 있음. 
			nxtC = 0;
		}
		else if (i == 5)
		{
			nxtR = 1;
			nxtC = 0;
		}
		else if (i == 10)
		{
			nxtR = 2;
			nxtC = 0;
		}
		else if (i == 15)
		{
			nxtR = 3;
			nxtC = 0;
		}
		board[0].push_back({ n, nxtR, nxtC });
	}

	// 2행
	board[1].push_back({ 13, 1, 1 });
	board[1].push_back({ 16, 1, 2 });
	board[1].push_back({ 19, 5, 0 });

	// 3행
	board[2].push_back({ 22, 2, 1 });
	board[2].push_back({ 24, 4, 0 });

	// 4행
	board[3].push_back({ 28, 3, 1 });
	board[3].push_back({ 27, 3, 2 });
	board[3].push_back({ 26, 4, 0 });

	// 5행
	board[4].push_back({ 25, 4, 1 });
	board[4].push_back({ 30, 4, 2 });
	board[4].push_back({ 35, 5, 0 });

	// 6행
	board[5].push_back({ 40, 5, 1 });
	// 끝
}

void Solve()
{
	vector<int> selectedMals;
	dfs(0, selectedMals);
	
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



*/
