// https://www.acmicpc.net/problem/2295

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

int N;
vector<long long> vecN;

// 이분탐색 중복 방지를 위해서 한번 검사한 값은 점프
unordered_map<long long, int> mapCheck;

void Input()
{
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		long long num;
		cin >> num;
		vecN.push_back(num);
	}
}

void Solve()
{
	std::sort(vecN.begin(), vecN.end());

	// a + b 로 구성된 vector 를 구성한다
	vector<long long> vecAB;
	vecAB.reserve(N);

	for (int f = 0; f < vecN.size(); ++f)
	{
		for (int s = f; s < vecN.size(); ++s)
		{
			vecAB.push_back(vecN[f] + vecN[s]);
		}
	}

	std::sort(vecAB.begin(), vecAB.end());

	//for (int i = 0; i < vecAB.size(); ++i)
	//{
	//	cout << vecAB[i] << ".";
	//}
	//cout << endl;

	long long answerV = 0;
	int k = 0;

	// vecN 을 돌면서, Big - Small 이 vecAB 안에 있는지 확인하면 된다.
	for (int bigIdx = vecN.size() - 1; bigIdx >= 1; --bigIdx)
	{
		for (int smallIdx = 0; smallIdx <= bigIdx; ++smallIdx)
		{
			long long LeftValue = vecN[bigIdx] - vecN[smallIdx];

			// Left 가 vecN 에 있는지 확인한다
			int st = 0;
			int ed = vecAB.size() - 1;

			while (st <= ed)
			{
				int mid = (st + ed) / 2;

				if (vecAB[mid] == LeftValue)
				{
					cout << vecN[bigIdx] << endl;
					return;
				}

				if (vecAB[mid] < LeftValue)
				{
					st = mid + 1;
				}
				else
				{
					ed = mid - 1;
				}
			}
		}
	}
}

void DEBUG()
{
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
