// https://www.acmicpc.net/problem/13397

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

int dRow[] = {-1, 1, 0,0};
int dCol[] =  {0, 0, -1,1};

int N, M;
vector<int> vecNum;

void Input()
{
	cin >> N >> M;

	for (int i = 0; i < N; ++i)
	{
		int InputN;
		cin >> InputN;
		vecNum.push_back(InputN);
	}
}

void DEBUG()
{
	
}

bool IsPossible(int val)
{
	int cnt = 1, minVal = INF, maxVal = INF * -1;

	for (int i = 0; i < N; ++i)
	{
		minVal = min(minVal, vecNum[i]);
		maxVal = max(maxVal, vecNum[i]);

		// 구간 점수가 val 보다 크다면 새로운 구간 
		if (maxVal - minVal > val)
		{
			minVal = maxVal = vecNum[i];
			cnt++;
		}
	}

	return cnt <= M;
}

void Solve()
{
	// 구간의 점수의 최대값을 어떤 수 'm' 으로 고정해놓고 구간을 나눠보는 방식
	// 구간 점수의 최댓값이 mid 일 때, 배열의 구간을 m개 이하로 나눌 수 있다면, 범위를 좁혀주면서 최소값을 찾아준다.

	int answer = 0;

	int left = 0;
	int right = 10000;

	while (left <= right)
	{
		int mid = (left + right) / 2;

		// 해당 mid 보다 더 큰 값을 만족시킬 수 있다는 의미
		// 지금은 최소값을 찾는 것이므로, 왼쪽으로 간다.
		if (IsPossible(mid))
		{
			answer = mid;
			right = mid - 1;
		}
		// 해당 mid 보다 큰값을 만족시킬 수 없다.
		// 즉, 해당 구간 점수를 만족시키는 M개 "보다 많은" 집함 --> 조건인 "M개 이하의 구간"에 맞지 않으므로 다시 조정해야 한다.
		else
			left = mid + 1; 
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
