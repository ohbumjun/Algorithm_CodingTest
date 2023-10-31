// https://www.acmicpc.net/problem/1613

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N , K;
vector<vector<int>> vecDist;

void Input()
{
    cin >> N >> K;

    vecDist.resize(N + 1);

    for (int i = 0; i <= N; ++i)
    {
        vecDist[i] = vector<int>(N + 1, INF);
        vecDist[i][i] = 0;
    }

    for (int i = 0; i < K; ++i)
    {
        int fC, sC;
        cin >> fC >> sC;
        vecDist[fC][sC] = 1;
        // vecDist[sC][fC] = -1;
    }

    for (int k = 1; k <= N; ++k)
    {
	    for (int st = 1; st <= N; ++st)
	    {
		    for (int ed = 1; ed <= N; ++ed)
		    {
                //if (vecDist[st][k] == INF || vecDist[k][ed] == INF)
                //    continue;
                vecDist[st][ed] = min(vecDist[st][ed], vecDist[st][k] + vecDist[k][ed]);
		    }
	    }
    }

    for (int st = 1; st <= N; ++st)
    {
        for (int ed = 1; ed <= N; ++ed)
        {
            if (vecDist[st][ed] != INF && vecDist[st][ed] > 0)
                vecDist[ed][st] = -vecDist[st][ed];
        }
    }

    int Test;
    cin >> Test;

    for (int i = 0; i < Test; ++i)
    {
        int stC = -1, edC = -1;
        cin >> stC >> edC;
        if (vecDist[stC][edC] == INF)
            cout << 0 << endl;
        else if (vecDist[stC][edC] < 0)
            cout << 1 << endl;
        else if (vecDist[stC][edC] > 0)
            cout << -1 << endl;
    }
}

void Solve()
{
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