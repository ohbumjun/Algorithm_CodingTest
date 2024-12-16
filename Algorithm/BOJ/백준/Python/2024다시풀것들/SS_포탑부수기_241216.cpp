// https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/description?page=3&pageSize=5

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

// N : 행
// M : 열
int N, M, K;
int totRow, totCol;

vector<vector<int>> Board;

// 가장 최근 공격 시간 저장
vector<vector<int>> lastAttackTurn;

// 해당 turn 에 공격에 개입되었는가
vector<vector<bool>> isInvolved;

// 우 / 하 / 좌 / 상 + 대각선 4방향
int dRow[] = {0, 1, 0, -1, -1, -1, 1, 1 };
int dCol[] = { 1, 0, -1, 0, 1, -1, -1, 1 };

void Input()
{
	cin >> N >> M >> K;
	totRow = N;
	totCol = M;

	Board.resize(N, vector<int>(M, 0));
	isInvolved.resize(N, vector<bool>(M, false));
	lastAttackTurn.resize(N, vector<int>(M, 0));

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < M; ++c)
			cin >> Board[r][c];
}


void Solve()
{
	/*
	* N * M보드 "모든" 위치에 포탑 존재
	* - 공격력 (+, - 가능)
	* - 공격력 0 이하가 되면, 포탑 부서지고, 공격 불가
	* - 최초 공격력 0 이하 포탑 존재 o
	*/

	/*
	* for K 번 턴
	*	for 하나의 턴 > 4가지 액션 반복
	* - 단. 부서지지 않은 포탑이 1개가 된다면, 그 즉시 중단
	*/
	for (int turn = 1; turn <= K; ++turn)
	{
		// 공격 개입 정보 reset
		for (int r = 0; r < totRow; ++r)
			for (int c = 0; c < totCol; ++c)
				isInvolved[r][c] = false;

		/*
		1) 공격자 선정
		a)- 부서지지 "않은" 포탑 중 !
			가장 약한 포탑이 "공격자" 로 선정
		- 공격자 선정 되면 (N + M) 만큼 공격력 증가
		b) 여러 개 ?
		- 가장 최근에 공격한 포탑이 가장 약한 포탑
		- 맨 처음, 모든 포탑은 시점 0 에 공격한 경험 존재
		c) 여러개 -> 행 + 열. 합 가장 큰 것.
		d) 여러개 -> "열" 값 가장 큰 것.
		*/
		vector<pair<int,int>> attackers;

		// 일단 가장 작은 공격력이 무엇인지 판단
		int minAttack = INT_MAX;
		for (int r = 0; r < totRow; ++r)
			for (int c = 0; c < totCol; ++c)
				if (Board[r][c] != 0 && Board[r][c] < minAttack)
					minAttack = Board[r][c];

		// 공격자 후보들을 모은다
		for (int r = 0; r < totRow; ++r)
			for (int c = 0; c < totCol; ++c)
				if (Board[r][c] == minAttack)
					attackers.push_back({ r, c });
		
		pair<int, int> attackInfo = attackers[0];

		for (int a = 1; a < attackers.size(); ++a)
		{
			int existingRow = attackInfo.first;
			int existingCol = attackInfo.second;

			int attackRow = attackers[a].first;
			int attackCol = attackers[a].second;

			// b) 여러 개 ?
			// -가장 최근에 공격한 포탑이 가장 약한 포탑
			// - 맨 처음, 모든 포탑은 시점 0 에 공격한 경험 존재
			// c) 여러개->행 + 열.합 가장 큰 것.
			// d) 여러개 -> "열" 값 가장 큰 것.

			// attackRow 에 해당하는 turn이 더 크면
			// 더 최근에 공격했다는 의미이므로 바꾼다.
			if (lastAttackTurn[existingRow][existingCol]
				< lastAttackTurn[attackRow][attackCol])
			{
				attackInfo = { attackRow, attackCol };
				continue;
			}
			else if (lastAttackTurn[existingRow][existingCol]
				> lastAttackTurn[attackRow][attackCol])
			{
				continue;
			}
			

			int existingSum = existingRow + existingCol;
			int attackSum = attackRow + attackCol;

			if (existingSum < attackSum)
			{
				attackInfo = { attackRow, attackCol };
				continue;
			}
			else if (existingSum > attackSum)
			{
				continue;
			}

			if (existingCol < attackCol)
			{
				attackInfo = { attackRow, attackCol };
				continue;
			}
			else if (existingCol > attackCol)
			{
				continue;
			}
		}
		
		int attackerRow = attackInfo.first;
		int attackerCol = attackInfo.second;

		// 마지막 공격 turn update
		lastAttackTurn[attackerRow][attackerCol] = turn;

		// 공격 개입 true
		isInvolved[attackerRow][attackerCol] = true;

		// 공격력 증가
		Board[attackerRow][attackerCol] += (totRow + totCol);

		int attackDamage = Board[attackerRow][attackerCol];

		/*
		2) 공격자 공격 + 공격대상 선정
		- 자신 제외 가장 강한 포탑 공격
		- a) 공격력 가장 높은 포탑
		- b) 공격한지 가장 오래된 것
		- c) 행,열 합 가장 "작은"
		- d) "열" 값 가장 "작은"
		*/
		vector<pair<int, int>> victims;

		// 일단 가장 큰 공격력이 무엇인지 판단
		int maxAttack = 0;
		for (int r = 0; r < totRow; ++r)
		{
			for (int c = 0; c < totCol; ++c)
			{
				// 공격자 제외.
				if (r == attackerRow && c == attackerCol)
					continue;
				if (Board[r][c] != 0 && Board[r][c] > maxAttack)
					maxAttack = Board[r][c];
			}
		}
			

		// 피해자 후보들을 모은다
		for (int r = 0; r < totRow; ++r)
			for (int c = 0; c < totCol; ++c)
				if (Board[r][c] == maxAttack)
					victims.push_back({ r, c });

		pair<int, int> victimInfo = victims[0];

		for (int v = 1; v < victims.size(); ++v)
		{
			int existingRow = victimInfo.first;
			int existingCol = victimInfo.second;

			int victimRow = victims[v].first;
			int victimCol = victims[v].second;

			if (lastAttackTurn[existingRow][existingCol]
				> lastAttackTurn[victimRow][victimCol])
			{
				victimInfo = { victimRow, victimCol };
				continue;
			}
			else if (lastAttackTurn[existingRow][existingCol]
			< lastAttackTurn[victimRow][victimCol])
			{
				continue;
			}

			int existingSum = existingRow + existingCol;
			int attackSum = victimRow + victimCol;

			if (existingSum > attackSum)
			{
				victimInfo = { victimRow, victimCol };
				continue;
			}
			else if (existingSum < attackSum)
			{
				continue;
			}

			if (existingCol > victimCol)
			{
				victimInfo = { victimRow, victimCol };
				continue;
			}
			else if (existingCol < victimCol)
			{
				continue;
			}
		}

		int victimRow = victimInfo.first;
		int victimCol = victimInfo.second;

		// 공격 개입 true
		isInvolved[victimRow][victimCol] = true;

		/*
		공격 종류 1) 레이저 공격
		- 레이저 공격이 안되면, 포탄 공격
		- 상하좌우 4개 방향
		- 부서진 포탑 지날 수 "없음" (주의)
		- 범위 벗어난 경우, 반대편으로 나옴
		- st : 공격자 위치 ~ ed : 공격대상 => 최단 경로로 공격
		- 만약 최단 경로 존재 X ? 포탄 공격
		- 만약 최단 경로 2개 이상 ? => 우/하/좌/상. 우선순위

		- 공격 대상 : "공격자 공격력" 만큼 "피해", 공격력 --
		- 최단 경로에 있던 포탑도 피해. "공격자 공격력 / 2"
		*/
		vector<vector<int>> bfsMap(totRow, vector<int>(totCol, INT_MAX));
		vector<vector<vector<int>>> pathBFS(totRow, 
			vector<vector<int>>(totCol));
		vector<int> pathToVictim;
		queue < tuple<int, int, int, vector<int>>> q;
		q.push({ attackerRow, attackerCol, 0, pathToVictim });

		while (!q.empty())
		{
			int curRow	= get<0>(q.front());
			int curCol	= get<1>(q.front());
			int curDist = get<2>(q.front());
			vector<int> curPath = get<3>(q.front());
			q.pop();

			// 우선순위만 고려 따라서 '=' 을 붙인다.
			if (curDist >= bfsMap[curRow][curCol])
				continue;

			bfsMap[curRow][curCol] = curDist;
			pathBFS[curRow][curCol] = curPath;

			for (int d = 0; d < 4; ++d)
			{
				int nxtRow = curRow + dRow[d];
				int nxtCol = curCol + dCol[d];

				// 범위 조정
				if (nxtRow >= totRow)
					nxtRow = 0;
				if (nxtRow < 0)
					nxtRow = totRow - 1;
				if (nxtCol >= totCol)
					nxtCol = 0;
				if (nxtCol < 0)
					nxtCol = totCol - 1;

				// 부서진 포탑
				if (Board[nxtRow][nxtCol] == 0)
					continue;

				curPath.push_back(d);
				q.push({nxtRow, nxtCol, curDist + 1, curPath});
				curPath.pop_back();
			}
		}

		pathToVictim = pathBFS[victimRow][victimCol];

		if (pathToVictim.size() == 0)
		{
			/*
			공격 종류 2) 포탄 공격
			- 공격대상 포탄 던짐 => 공격대상 : 공격력 만큼 --
			- 주위 8방향도 피해
				- 공격력 / 2
				- 공격자.는 피해 X
				- 범위 벗어남 => 반대편 격자로
				- 부서진 포탑은 X
			*/
			vector<pair<int, int>> potanAttacked;
			potanAttacked.push_back({ victimRow, victimCol });
			for (int d = 0; d < 8; ++d)
			{
				int nxtRow = victimRow + dRow[d];
				int nxtCol = victimCol + dCol[d];

				// 범위 조정
				if (nxtRow >= totRow)
					nxtRow = 0;
				if (nxtRow < 0)
					nxtRow = totRow - 1;
				if (nxtCol >= totCol)
					nxtCol = 0;
				if (nxtCol < 0)
					nxtCol = totCol - 1;
				// 부서진 포탑
				if (Board[nxtRow][nxtCol] == 0)
					continue;
				// 공격자 X
				if (nxtRow == attackerRow && nxtCol == attackerCol)
					continue;
				potanAttacked.push_back({ nxtRow, nxtCol });
				// if (nxtRow == victimRow && nxtCol == victimCol)
				// 	Board[nxtRow][nxtCol] -= attackDamage;
				// else
				// 	Board[nxtRow][nxtCol] -= attackDamage / 2;
			}

			for (int idx = 0; idx < potanAttacked.size(); ++idx)
			{
				const pair<int, int>& curPos = potanAttacked[idx];
				int curR = curPos.first;
				int curC = curPos.second;

				// 공격 개입 표시
				isInvolved[curR][curC] = true;

				if (curR == victimRow && curC == victimCol)
					Board[curR][curC] -= attackDamage;
				else
					Board[curR][curC] -= attackDamage / 2;
			}
		}
		else
		{
			// 레이저 공격 실행
			// - st : 공격자 위치 ~ed : 공격대상 = > 최단 경로로 공격
			// - 공격 대상 : "공격자 공격력" 만큼 "피해", 공격력--
			// - 최단 경로에 있던 포탑도 피해. "공격자 공격력 / 2"
			int curAttackRow = attackerRow;
			int curAttackCol = attackerCol;

			for (int idx = 0; idx < pathToVictim.size(); ++idx)
			{
				int curD = pathToVictim[idx];
				int nxtRow = curAttackRow + dRow[curD];
				int nxtCol = curAttackCol + dCol[curD];

				// 범위 조정
				if (nxtRow >= totRow)
					nxtRow = 0;
				if (nxtRow < 0)
					nxtRow = totRow - 1;
				if (nxtCol >= totCol)
					nxtCol = 0;
				if (nxtCol < 0)
					nxtCol = totCol - 1;

				// 공격 개입 표시
				isInvolved[nxtRow][nxtCol] = true;

				if (nxtRow == victimRow && nxtCol == victimCol)
					Board[nxtRow][nxtCol] -= attackDamage;
				else
					Board[nxtRow][nxtCol] -= attackDamage / 2;

				curAttackRow = nxtRow;
				curAttackCol = nxtCol;
			}
		}

		/*
		포탑 부서짐
		- 공격력 0 이하가 되면 되면, 부서짐
		*-단.부서지지 않은 포탑이 1개가 된다면, 그 즉시 중단
		*/
		int notBrokenCnt = 0;
		for (int r = 0; r < totRow; ++r)
		{
			for (int c = 0; c < totCol; ++c)
			{
				if (Board[r][c] < 0)
					Board[r][c] = 0;
				if (Board[r][c] > 0)
					notBrokenCnt++;
			}
		}

		if (notBrokenCnt == 1)
			break;

		/*
		포탑 정비
		- 공격 모두 끝난 이후 진행
		- 공격자, 혹은 피해자. 제외 다른 포탑들 공격력 + 1
		*/
		for (int r = 0; r < totRow; ++r)
		{
			for (int c = 0; c < totCol; ++c)
			{
				if (Board[r][c] == 0)
					continue;
				if (isInvolved[r][c])
					continue;
				Board[r][c] += 1;
			}
		}

		// Debug
		// cout << " --------- " << endl;
		// for (int r = 0; r < totRow; ++r) {
		// 	for (int c = 0; c < totCol; ++c)
		// 		cout << Board[r][c] << " ";
		// 	cout << endl;
		// }
	}

	// 가장 강한 공격력 출력하기.
	int maxAttack = 0;
	for (int r = 0; r < totRow; ++r)
		for (int c = 0; c < totCol; ++c)
			if (Board[r][c] != 0 && Board[r][c] > maxAttack)
				maxAttack = Board[r][c];

	cout << maxAttack << endl;
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


