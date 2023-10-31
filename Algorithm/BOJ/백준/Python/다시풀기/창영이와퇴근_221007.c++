// https://www.acmicpc.net/problem/22116

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

int dRow[] = { -1, 1, 0,0 };
int dCol[]   = { 0, 0, -1, 1 };

int N;
vector<vector<int>> vecLand;

void Input()
{
	cin >> N;
	vecLand.resize(N);

	for (int i = 0; i < N; ++i)
		vecLand[i].resize(N);

	for (int r = 0; r < N; ++r)
	{
		for (int c = 0; c < N; ++c)
		{
			int elem = 0;
			cin >> elem;
			vecLand[r][c] = elem;
		}
	}
}

void Solve()
{
	vector<vector<int>> vecMinDiff;

	vecMinDiff.resize(N);

	for (int i = 0; i < N; ++i)
		vecMinDiff[i] = vector<int>(N, INF);

	priority_queue<pair<int, pair<int, int>>> Queue;
	Queue.push({ 0, {0,0} });

	while (!Queue.empty())
	{
		auto [curDiff, posInfo] = Queue.top();
		Queue.pop();

		curDiff *= -1;
		int curR = posInfo.first;
		int curC = posInfo.second;

		if (curDiff >= vecMinDiff[curR][curC])
			continue;

		cout << "curDiff, curR, curC : " << curDiff << "," << curC << "," << curC << endl;

		vecMinDiff[curR][curC] = curDiff;

		for (int k = 0; k < 4; ++k)
		{
			int nxtR = curR + dRow[k];
			int nxtC = curC + dCol[k];

			if (nxtR < 0 || nxtC < 0 || nxtR >= N || nxtC >= N)
				continue;

			if (vecMinDiff[nxtR][nxtC] != INF)
				continue;

			int minDiff = curDiff;
			int nxtDiff = vecLand[curR][curC] - vecLand[nxtR][nxtC];

			if (nxtDiff < 0)
				nxtDiff *= -1;

			if (nxtDiff > minDiff)
				minDiff = nxtDiff;

			Queue.push({ -minDiff, {nxtR,nxtC} });
		}
	}

	cout << vecMinDiff[N - 1][N - 1];
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