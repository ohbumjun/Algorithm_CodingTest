// https://www.acmicpc.net/problem/11066

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <array>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>
#include <cstring>
#include <string>

#define endl "\n"
#define MAX 100000+1
#define INF int(1e9)

using namespace std;

int N;
int T;
// DP[a][b] : a 에서 b  idx 까지의 파일들을 합치는 최소 비용
int DP[501][501];

// 합치는데 드는 비용
// - 1개 원소는 합치는데 드는 비용이 0일 것이다.
// - 여기서 중요한 점은, 합치는 비용을 누적시키는 과정이다.
int SumCost(int stIdx, int edIdx, const vector<int>& vecNums);

void Input()
{
	cin >> T;
}

void Solve()
{
	for (int t = 0; t < T; ++t)
	{
		int N;
		cin >> N;

		vector<int> vecNums;

		for (int n = 0; n < N; ++n)
		{
			int num;
			cin >> num;
			vecNums.push_back(num);
		}

		memset(DP, -1, sizeof(DP));

		int Cost = SumCost(0, N - 1, vecNums);

		cout << Cost << endl;
	}
}

int SumCost(int stIdx, int edIdx, const vector<int>& vecNums)
{
	if (DP[stIdx][edIdx] != -1)
		return  DP[stIdx][edIdx];

	if (stIdx == edIdx)
	{
		DP[stIdx][edIdx] = 0;
		return 0;
	}

	int minCost = INF;

	int CostSum = 0;

	for (int idx = stIdx; idx <= edIdx; ++idx)
		CostSum += vecNums[idx];

	for (int idx = stIdx; idx < edIdx; ++idx)
	{
		// idx : 분할 기준
		int Cost1 = SumCost(stIdx, idx, vecNums);

		int Cost2 = SumCost(idx + 1, edIdx, vecNums);

		// Cost1 : 첫번째 영역 파일들 합치는 비용
		// Cost2 : 두번째 영역 파일들 합치는 비용
		// Cost3 : 해당 영역들 파일들의 비용 합 (최종 합치는 과정이라고 생각하면 된다.)
		int TmpCost = Cost1 + Cost2 + CostSum;

		minCost = min(minCost, TmpCost);
	}

	DP[stIdx][edIdx] = minCost;

	return minCost;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();
	Solve();

	return 0;
}