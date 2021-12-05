#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include <algorithm>
#include <functional>
#include<queue>
 
#define endl "\n"
#define NODE_MAX 500 + 1
#define EDGE_MAX 6000 + 1
#define INF int(1e9)

using namespace std;

int N, M, start;
vector<pair<pair<int, int>, int>> edges;
long long dist[NODE_MAX];


void input()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int stN, edN, cost;
        cin >> stN >> edN >> cost;
        edges.push_back(make_pair(make_pair(stN, edN), cost));
    }

    // 최단 거리 정보 초기화
    fill_n(dist, NODE_MAX, INF);
}

void solve(int stN)
{
    dist[stN] = 0;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int stN  = edges[j].first.first;
            int edN = edges[j].first.second;
            int cost = edges[j].second;
            if (dist[stN] != INF && dist[edN] > dist[stN] + cost)
            {
                dist[edN] = dist[stN] + cost;
            }
        }
    }
    for (int j = 0; j < M; j++)
    {
        int stN = edges[j].first.first;
        int edN = edges[j].first.second;
        int cost = edges[j].second;
        if (dist[stN] != INF && dist[edN] > dist[stN] + cost)
        {
            cout << -1 << endl;
            return;
        }
    }
    for (int i = 2; i <= N; i++)
    {
        if (dist[i] == INF)
            cout << -1 << "\n";
        else
            cout << dist[i] << "\n";
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
     freopen("input_C.txt", "r", stdin);
   input();
   solve(1);
 
    return 0;
}


