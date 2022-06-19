// 1번째 방식 : 2차원 배열
// dp[i][j] => 내가 i번째 Idx 의 문제까지 풀수 있고, j의 시간이 주어졌을 때 얻을 수 있는 최대 점수 

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

int N, M;
vector<int> dp[101]; // dp[i][j] : i번 문제까지 풀고 있고, j라는 제한 시간이 주어졌을 때 얻을 수 있는 최대 점수
vector<pair<int, int>> vecProb;

void Input()
{
    cin >> N >> M;

	int score, time;
    vecProb.resize(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        cin >> score >> time;
        vecProb[i] = make_pair(score, time);
    }
}

void Solve()
{
	// dp[i][j] : i 시간 안에, j 개 문제 중 풀 수 있는 최대 점수
	// 매번 모든 문제를 돌면서
    for (int i = 0; i <= N; ++i)
        dp[i].resize(M + 1);

    for (int i = 1; i <= N; ++i)
    {
        int score = vecProb[i].first;
        int time  = vecProb[i].second;

        // 이전 행 내용을, 그대로 복사해서 세팅해야 한다.
        dp[i] = dp[i - 1];

        // 해당 문제를 푼다라고 가정한다.
        for (int t = time; t <= M; ++t)
        {
            dp[i][t] = max(dp[i][t], dp[i - 1][t - time] + score);
        }
    }

    cout << dp[N][M];
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

// 2번째 방식 : 1 차원 배열
// dp[j] : j 라는 제한 시간이 주어졌을 때, 내가 얻을 수 있는 최대 점수 
// 앞에서부터 진행하면 중복 , 따라서 뒤에서부터 진행하여 중복을 방지한다.

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

int N, M;
vector<int> dp; // dp[j] : j번째 제한 시간까지 얻을 수 있는 최대 점수 
vector<pair<int, int>> vecProb;

void Input()
{
    cin >> N >> M;

    dp.resize(M + 1);

	int score, time;
    vecProb.resize(N + 1);

    for (int i = 1; i <= N; ++i)
    {
        cin >> score >> time;
        vecProb[i] = make_pair(score, time);
    }
}

void Solve()
{
    for (int i = 1; i <= N; ++i)
    {
        int score = vecProb[i].first;
        int time = vecProb[i].second;

        for (int t = M; t >= time; --t)
        {
            dp[t] = max(dp[t], dp[t - time] + score);
        }
    }

    cout << dp[M];
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