// https://www.acmicpc.net/problem/13975

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

// 파일을 합치는 조건이 명시되어 있지 않다.
// - 따라서, 연속적이지 않은 파일들끼리 합쳐도 된다.
// - 최대한 적은 비용으로 합치려면, 합치는 파일의 크기가 작으면 된다.
// - 파일 크기대로 오름 차순
// - 우선 순위 큐를 사용
// - 2개를 빼서 합치고, 다시 넣고
// - 이러한 과정을 반복할 것이다.

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
		priority_queue<long long, vector<long long>, std::greater<long long>> queue;

		for (int n = 0; n < N; ++n)
		{
			long long num;
			cin >> num;
			queue.push(num);
		}

        // 정답의 범위를 고려하여 long long 으로 선언해야 한다.
		long long totSum = 0;

		while (queue.size() > 1)
		{
			long long f = queue.top();
			queue.pop();
			long long s = queue.top();
			queue.pop();
			long long sum = f + s;
			queue.push(sum);
			totSum += sum;
		}

		cout << totSum << endl;
	}
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