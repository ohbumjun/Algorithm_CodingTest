// https://www.acmicpc.net/problem/12892

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

int N,D;

void Input()
{
	cin >> N >> D;
}

void Solve()
{
	// 가격 기준 오름차순 정렬 정렬 
	// 그룹을 나누고 그에 대해서 여러번 계산 실행
	long long answer = 0;

	std::vector<pair<long long, long long>> vecInfos;

	for (int i = 0; i < N; ++i)
	{
		long long price, happiness;

		cin >> price >> happiness;

		vecInfos.push_back(make_pair(price, happiness));
	}

	std::sort(vecInfos.begin(), vecInfos.end());

	// for (const auto& [price, happiness] : vecInfos)
	// 	cout << "price, happiness : " << price << "," << happiness << endl;

	long long tmp = vecInfos[0].second;
	int ed = 1;

	for (int st = 0; st < N; ++st)
	{
		while (ed < N && vecInfos[ed].first < vecInfos[st].first + D)
		{
			tmp += vecInfos[ed].second;
			++ed;
		}

		if (tmp > answer)
			answer = tmp;

		tmp -= vecInfos[st].second;
	}

	cout << answer << endl;
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