// https://www.acmicpc.net/problem/9084

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
#define MAX 1000000+1
#define INF int(1e9)

using namespace std;

int T;
int N, M;

void Input()
{
    cin >> T;

}

void Solve()
{
	for (int i = 0; i < T; ++i)
	{
        vector<int> vecCoins;
        vector<int> vecDP;
        vecCoins.reserve(N);

        cin >> N;

        for (int j = 0; j < N; ++j)
        {
            int cInputN;
            cin >> cInputN;
            vecCoins.push_back(cInputN);
        }

        cin >> M;

        // N개의 Coin 을 이용해서
        // M 원을 만들어야 한다.
        vecDP.resize(M + 1);

        // dp 초기값을 1로 줘야 한다.
        vecDP[0] = 1;

        // 각 동전을 순회하면서
        // dp 정보를 채워준다.
        for (int cIdx = 0; cIdx < N; ++cIdx)
        {
            // 조합을 이용해서 채우기
	        for (int w = vecCoins[cIdx]; w <= M; w += 1)
	        {
                vecDP[w] += vecDP[w - vecCoins[cIdx]];
	        }
        }

        cout << vecDP[M] << endl;
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