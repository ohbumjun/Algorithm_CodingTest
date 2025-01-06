// https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek?page=4&pageSize=5

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>
#include <sstream>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;

int T;
int x, y;

void Input()
{
	cin >> T;
}

void Solve()
{
	// 맨 처음에는 1 만큼 이동 가능
	// dp[x] : x 칸 까지 이동하는 최소 거리 ?

	// 첫 이동거리와 마지막 이동거리는 1
	// 이동 거리는 직전 이동 거리 k 에 대해서 k -1, k, k+1 중 하나로 이동 가능

	// 자. 결국 해당 문제는 규칙을 잘 발견할 수 있는가에 대한 문제이다.

	// 그러면 1, 2, 3, ... (n-1), n, (n-1), ... 3, 2, 1 이런식으로 이동하게 되면
	// 작동횟수에 대해서 최대로 이동할 수 있다.
	// 1) 늘릴 때는 계속 늘리고
	// 2) 줄일 때는 계속 줄이고

	// 그러면 이동횟수가 짝수일 때는 어떨까 ?
	// 2 : 1, 1 (2)
	// 4 : 1, 2, 2, 1 (6)
	// 6 : 1, 2, 3, 3, 2, 1 (12)
	// 8 : 1, 2, 3, 4, 4, 3, 2, 1 (20)

	// 이와 같이, 이전 짝수에 비해 i/2 에 2번 추가된다.
	// dp[i] = dp[i-2] + (i/2) * 2;

	// 이동 횟수가 홀수일때는 ?
	// 1 : 1 (1)
	// 3 : 1 2 1 (4)
	// 5 : 1 2 3 2 1 (9)
	// 7 : 1 2 3 4 3 2 1 (16)
	// 9 : 1 2 3 4 5 4 3 2 1 (25)
	// 즉, 이전 홀수 + (i/2) + (i/2 + 1) 이다.

	// dp[i] : 이동횟수가 i 일 때, 최대 이동 거리
	// 자. 이제 dp 를 맨 처음 만들 때, 범위를 어떤 식으로 설정해야 할 지 모르겠다...
	// 2^31 은 몇번 이동으로 가능한가 ? 어림잡아서 해보면 되지 않을까 ?
	long long max = 100000;
	vector<long long> dp(max);
	dp[0] = 0;
	dp[1] = 1;
	for (long long i = 2; i < max;++i)
	{
		if (i % 2 == 0)
		{
			long long nxt = dp[i - 2] + (i / 2) * 2;
			dp[i] = nxt;
		}
		else
		{
			long long nxt = dp[i - 2] + (i / 2) + (i / 2 + 1);
			dp[i] = nxt;
		}
	}

	for (int t = 0; t < T; ++t)
	{
		// 이후 입력 x,y 가 주어지면, y - x 를 통해 dist 를 구한다
		// 이후, dp 에서 i번째가 자기보다 작거나 같고, i+1번째가 자기보다 큰 경우를 찾아 'i' 을 출력하면 된다.
		cin >> x >> y;
		long long dist = y - x;

		for (long long num = 0; num < max; ++num)
		{
			if (dp[num] >= dist)
			{
				cout << num << endl;
				break;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}


