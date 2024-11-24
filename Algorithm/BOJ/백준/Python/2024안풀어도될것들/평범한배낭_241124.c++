// https://www.acmicpc.net/problem/12865

// 1번째 방법 : 2차원 배열 활용하기 ---
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

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, K;
vector<int> dp[1001];
vector<pair<int, int>> vecProb;

void Input()
{
    cin >> N >> K;

    vecProb.resize(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        int weight = 0, value = 0;
        cin >> weight >> value;
        vecProb[i] = make_pair(weight, value);
    }
}

void Solve()
{
	// dp[i][j] : i 번째 문제를 풀 때, 제한시간 j 가 주어졌을 경우, 얻을 수 있는 최대 점수 
	// 매번 모든 문제를 돌면서
    for (int i = 0; i <= N; ++i)
        dp[i].resize(K + 1);

    for (int i = 1; i <= N; ++i)
    {
        int weight = vecProb[i].first;
        int value   = vecProb[i].second;

        dp[i] = dp[i - 1];

        // 해당 문제를 푼다라고 가정한다.
        for (int w = weight; w <= K; ++w)
        {
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value);
        }
    }

    cout << dp[N][K];
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

// 2번째 방법 : 1차원 배열 활용하기 ---
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

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, K;
vector<int> dp;
vector<pair<int, int>> vecProb;

void Input()
{
    cin >> N >> K;

    // dp[i] : 제한 시간 i 안에 얻을 수 있는 최대 점수 
	dp.resize(K+1);

    vecProb.resize(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        int weight = 0, value = 0;
        cin >> weight >> value;
        vecProb[i] = make_pair(weight, value);
    }
}

void Solve()
{
    for (int i = 1; i <= N; ++i)
    {
        int weight = vecProb[i].first;
        int value   = vecProb[i].second;

        dp[i] = dp[i - 1];

        // 해당 문제를 푼다라고 가정한다.
        for (int w = K; w >= weight; --w)
        {
            dp[w] = max(dp[w], dp[w - weight] + value);
        }
    }

    cout << dp[K];
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