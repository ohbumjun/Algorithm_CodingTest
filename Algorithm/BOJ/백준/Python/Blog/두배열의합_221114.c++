// https://www.acmicpc.net/problem/2143

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

long long T, N, M;
vector<long long> vecA;
vector<long long> vecB;

void Input()
{
	cin >> T;
	cin >> N;

	vecA.reserve(1000 * 1000);
	vecB.reserve(1000 * 1000);

	for (int i = 0; i < N; ++i)
	{
		long long num;
		cin >> num;
		vecA.push_back(num);
	}

	cin >> M;

	for (int i = 0; i < M; ++i)
	{
		long long num;
		cin >> num;
		vecB.push_back(num);
	}
}

void Solve()
{
	long long answer = 0;

	int sizeA = vecA.size();

	for (int i = 0; i < sizeA - 1; ++i)
	{
		long long sumA = vecA[i];
		for (int j = i + 1; j < sizeA; ++j)
		{
			sumA += vecA[j];
			vecA.push_back(sumA);
		}
	}

	int sizeB = vecB.size();

	for (int i = 0; i < sizeB - 1; ++i)
	{
		long long sumB = vecB[i];

		for (int j = i + 1; j < sizeB; ++j)
		{
			sumB += vecB[j];

			vecB.push_back(sumB);
		}
	}

	sort(vecA.begin(), vecA.end());
	sort(vecB.begin(), vecB.end());

	for (int i = 0; i < vecA.size(); ++i)
	{
		long long target = T - vecA[i];
		auto lower = lower_bound(vecB.begin(), vecB.end(), target);
		auto upper = upper_bound(vecB.begin(), vecB.end(), target);

		answer += (upper - lower);
	}

	cout << answer << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}