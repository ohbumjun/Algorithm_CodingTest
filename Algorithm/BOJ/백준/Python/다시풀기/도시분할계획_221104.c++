// https://www.acmicpc.net/problem/1647

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <stack>
#include <math.h>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define MAX 100000+1
#define INF int(1e9)

using namespace std;

int N, M;
vector<tuple<int, int, int>> vecPath; // 비용, st, ed
vector<int> vecParent;

void Input()
{
	cin >> N >> M;

	vecParent.resize(N + 1);

	for (int i = 0; i <= N; ++i)
		vecParent[i] = i;

	for (int i = 0; i < M; ++i)
	{
		int st, ed, cost;
		cin >> st >> ed >> cost;
		vecPath.push_back(make_tuple(cost, st, ed));
	}
}

int find_parent(int n)
{
	int pA = vecParent[n];

	if (pA != n)
		pA = find_parent(pA);

	return pA;
}

void union_parent(int a, int b)
{
	int pA = find_parent(a);
	int pB = find_parent(b);

	if (pA > pB)
		vecParent[a] = pB;
	else
		vecParent[b] = pA;
}

void Solve()
{
	int sumCost = 0;
	int maxPath = 0;

	sort(vecPath.begin(), vecPath.end());

	// 싸이클 없이 모두 연결
	// 가장 큰 비용의 간선 비용 Update
	// 모든 간선 비용 Sum
	// Sum - Max
	for (const auto& [cost, st, ed] : vecPath)
	{
		int pSt = find_parent(st);
		int pEd = find_parent(ed);
		
		if (pSt == pEd)
			continue;

		sumCost += cost;

		maxPath = max(maxPath, cost);

		union_parent(pSt, pEd);

		// cout << "st, ed, cost : " << st << "," << ed << "," << cost << endl;
		// for (int i = 1; i <= N; ++i)
		// 	cout << vecParent[i] << ".";
		// cout << endl;
		// cout << endl;
	}



	cout << sumCost - maxPath << endl;
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