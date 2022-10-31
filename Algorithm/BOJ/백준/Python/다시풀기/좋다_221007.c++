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
				// 어차피 st == i 혹은 ed == i에 걸리는 경우는 둘 중 하나 이상이 0인 경우이다.
				// 그려면 i 는 지금 증가하고 있으니, 즉, 앞에서부터 오른쪽으로 오면서, 검사하고 있으니
				// st == i 인 경우는, st 를 증가시켜서 우측을 검사하겠다는 것
				// 자 너가 생각한 대로 st - 1, st - 2 에도 같은 녀석이 있을 수 있다. 안다. 하지만, 그렇기 때문에
				// 지금 i 를 앞에서부터 증가시키면서 오는 것이다. 어차피 이렇게 하면 st - 1, st - 2 인 경우의 수는 다 고려가 되니까
				// 반대로 ed == i인 경우는 , st 가 0인 경우가 된다. 그러면 이 경우는 왼쪽으로 내려서 검사할 것이라는 의미이다.
				// 어차피 ed + 1, ed + 2 인 경우는 i가 증가하면서 자연스레 검사 범위에 들어가기 때문이다.
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

/*
<틀린 범위>

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

int N;
vector<long long> vecN;
unordered_map<long long, int> mapNumNum;
unordered_map<long long, int> mapSumV;

void Input()
{
	cin >> N;

	vecN.reserve(N);

	for (int i = 0; i < N; ++i)
	{
		long long newN;
		cin >> newN;
		mapNumNum[newN] += 1;
		vecN.push_back(newN);
	}
}

void Solve()
{
	int Answer = 0;

	sort(vecN.begin(), vecN.end());

	// 1. 먼저 0만 2개 존재하는 상황 방지
	// if (vecN.size() == 2 && mapNumNum[0] == 2)
	// {
	// 	cout << 0 << endl;
	// 	exit(0);
	// }

	// 이차원 for 문을 돌며 모든 합 경우의 수를 찾는다.
	// 이후 각 원소를 돌며 합 경우에 수에 속하는지 확인
	// 1. 0이 있을 경우, mapNumNum 이 2 이상일 때만 
	// 2. 0이 있고 mapNumNum이 1이면 continue;
	// 3. 0이 없으면 그냥 모두 더하기 
	for (int f = 0; f < N - 1; ++f)
	{
		for (int s = f + 1; s < N; ++s)
		{
			// 0이 2개인 경우, + 가 되게 된다. 이를 방지
			if (vecN[f] == 0 && vecN[f] == 0 && mapNumNum[0] == 2)
				continue;

			// vecN[f]가 0일 때
			if (vecN[f] == 0)
			{
				if (mapNumNum[vecN[s]] < 2)
					continue;
			}

			// vecN[s]가 0일 때
			if (vecN[s] == 0)
			{
				if (mapNumNum[vecN[f]] < 2)
					continue;
			}


			long long newS = vecN[s] + vecN[f];

			mapSumV[newS] = 1;
		}
	}

	// 0과 자기 자신만을 더한 경우는 고려되지 않는다.
	set<long long> setAnsNum (vecN.begin(), vecN.end());

	auto iter      = setAnsNum.begin();
	auto iterEnd = setAnsNum.end();
	
	for (; iter != iterEnd; ++iter)
	{
		long long curV = *iter;

		if (mapSumV[curV] == 1)
			Answer += mapNumNum[curV];
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

*/