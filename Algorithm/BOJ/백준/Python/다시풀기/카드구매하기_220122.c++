#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int N;
std::vector<int> DP;
std::vector<int> Packs;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> N;
    int Offset = 4;

    DP = std::vector<int>(N + Offset, 0);
    Packs = std::vector<int>(N + 1, 0);

    for (int i = 0; i < N; i++)
    {
        int Input;
        cin >> Input;
        Packs[i+1] = Input;
    }

    for (int i = Offset; i < N + 4; i++)
    {
        // 1개 
        DP[i] = DP[i - 1] + Packs[1];
        for (int j = 2; j <= i - 3; j++)
        {
            // 2개
            if (DP[i] < DP[i - j] + Packs[j])
                DP[i] = DP[i - j] + Packs[j];
        }
    }

    cout << DP[N - 1 + 4];
    return 0;
}


