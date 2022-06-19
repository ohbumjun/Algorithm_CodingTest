// https://www.acmicpc.net/problem/12865

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

// 1번째 풀이 : 오답 ==> 왜 ? 같은 보석을 여러 개 넣을 수 없기 때문에
// 그런데 아래의 코드는, 같은 보석을 여러 번 담을 수 있다라는 가정 하에서 푼 문제 이다.
#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, K;
vector<int> dp;
vector<pair<int, int>> vecP;

void Input()
{
    cin >> N >> K;

    int weight, value;

    for (int i = 0; i < N; ++i)
    {
        cin >> weight >> value;
        vecP.push_back(make_pair(weight, value));
    }
}

void Solve()
{
    dp.resize(K + 1);

    // 1개 각각이 물건이 해당 가방에 들고 있다고 가정하면서
    // 해당 가방 내의 최대 가치를 Update
    for (int p = 0; p < vecP.size(); ++p)
    {
        int curW = vecP[p].first;
        int curV  = vecP[p].second;
        for (int i = curW; i <= K; ++i)
            dp[i] = max(dp[i - curW] + curV, dp[i]);
    }

    cout << dp[K];
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    // freopen("input_c.txt", "r", stdin);

    Input();
    Solve();

    return 0;
}