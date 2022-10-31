// https://www.acmicpc.net/problem/1253

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
vector<int> vecNums;

void Input()
{
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int num;
		cin >> num;
		vecNums.push_back(num);
	}
}

void Solve()
{
	// 이분 탐색을 수행
	// 먼저 오름 차순 정렬 (set 자동 정렬)
	int Answer = 0;

	std::sort(vecNums.begin(), vecNums.end());

	for (int i = 0; i < vecNums.size(); ++i)
	{
		int st = 0;
		int ed = vecNums.size() - 1;

		while (st < ed)
		{
			int Sum = vecNums[st] + vecNums[ed];

			if (Sum == vecNums[i])
			{
				if (i != st && i != ed)
				{
					Answer += 1;
					break;
				}
				else if (st == i)
					st++;
				else if (ed == i)
					ed--;
			}

			else if (Sum >= vecNums[i])
			{
				ed -= 1;
			}
			else
			{
				st += 1; //
			}
		}
	}

	cout << Answer << endl;
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