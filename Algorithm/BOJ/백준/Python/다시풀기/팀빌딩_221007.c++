// https://www.acmicpc.net/problem/22945

// 투 포인터 이용
// 처음에는 양 끝으로 배치
// 점차 더 큰 값이 있는 가운데 쪽으로 이동시키면서 값 비교하기 

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
vector<int> vecAbility;

void Input()
{
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int Ability;
		cin >> Ability;
		vecAbility.push_back(Ability);
	}
}

void Solve()
{
	// 2개의 포인터를 양쪽에 둘 것이다
	// min 에 해당하는 포인터를 가운데 쪽으로 이동
	int st = 0;
	int ed = vecAbility.size() - 1;

	int Answer = 0;

	while (st < ed + 1)
	{
		int val = (ed - st - 1) * min(vecAbility[st], vecAbility[ed]);

		// cout << "st , ed : " << st << "." << ed << endl;
		// cout << "Answer, val : " << Answer << "." << val << endl;

		Answer = max(Answer, val);

		if (vecAbility[st] <= vecAbility[ed])
			st += 1;
		else
			ed -= 1;
	}

	cout << Answer << endl;
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