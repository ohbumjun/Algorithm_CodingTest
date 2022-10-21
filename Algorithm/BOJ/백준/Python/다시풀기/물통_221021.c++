// https://www.acmicpc.net/problem/2251

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define MAX 100000+1
#define INF int(1e9)

using namespace std;

int A, B, C;
vector<int> vecOrigin;
set<int> setAns;
unordered_map<int, int> mapCups;

void Input()
{
	cin >> A >> B >> C;

	vecOrigin.push_back(A);
	vecOrigin.push_back(B);
	vecOrigin.push_back(C);
}

void DFS(vector<int>& vecCups)
{
	// for (const auto& e : vecCups)
	// 	cout << e << ".";
	// cout << endl;

	int mKey = vecCups[0] * 201 * 201 + vecCups[1] * 201 + vecCups[2];

	if (mapCups[mKey] == 1)
		return;

	mapCups[mKey] = 1;

	if (vecCups[0] == 0)
		setAns.insert(vecCups[2]);

	for (int curIdx = 0; curIdx < 3; ++curIdx)
	{
		for (int i = 0; i < 3; ++i)
		{
			if (curIdx == i)
				continue;

			// curIdx 에서 i 번째로 통을 들이붇는다.
			int curOriginCup = vecCups[curIdx];
			int curCup = vecCups[curIdx];

			int targetOriginCup = vecCups[i];
			int targetCup = vecCups[i];

			// cout << "bef => i, curCup, targetCup : " << i << "," << curCup << "," << targetCup << endl;

			// 원래 물통이 텅 빌 때까지 , 혹은 붇는 대상이 가득 차지 않을 때까지 
			while (curCup > 0 && targetCup < vecOrigin[i])
			{
				curCup--;
				targetCup++;
			}

			vecCups[curIdx] = curCup;
			vecCups[i] = targetCup;

			// cout << "aft => curCup, targetCup : " << i << "," << curCup << "," << targetCup << endl;

			DFS(vecCups);

			// 원상복구
			vecCups[curIdx] = curOriginCup;
			vecCups[i] = targetOriginCup;
		}
	}
}

void Solve()
{
	vector<int> vecCups;
	vecCups.push_back(0);
	vecCups.push_back(0);
	vecCups.push_back(vecOrigin[2]);

	DFS(vecCups);

	vector<int> vecAns;

	auto iter      = setAns.begin();
	auto iterEnd = setAns.end();

	for (; iter != iterEnd; ++iter)
		cout << *iter << " ";
	cout << endl;
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