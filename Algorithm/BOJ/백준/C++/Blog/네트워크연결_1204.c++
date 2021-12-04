#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include <algorithm>
#include<queue>
 
#define endl "\n"
#define EDGE_MAX 100000 + 1
#define NODE_MAX 1000 + 1
using namespace std;

int N, M, ans;
vector<struct Edge> edges;
 
// Kruskal 알고리즘 
int get_parent(int parent [], int x)
{
    if (parent[x] != x)
        parent[x] = get_parent(parent, parent[x]);
    return parent[x];
}

void union_parent(int parent[], int x, int y)
{
    int px = get_parent(parent, x);
    int py = get_parent(parent, y);
    if (px < py)
        parent[py] = px;
    else
        parent[px] = py;
}

struct Edge
{
    int node[2];
    int distance;
    Edge(int a, int b, int dist)
    {
        node[0] = a;
        node[1] = b;
        distance = dist;
    }
    bool operator < (Edge& edge)
    {
        return distance < edge.distance;
    }
};

void input()
{
    cin >> N;
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int stN, edN, cost;
        cin >> stN >> edN >> cost;
        edges.push_back(Edge(stN, edN, cost));
    }
}

void solution()
{
    // 부모 초기화
    int parent[NODE_MAX];
    for (int i = 0; i < NODE_MAX; i++)
    {
        parent[i] = i;
    }

    // 간선 정렬
    sort(edges.begin(), edges.end());

    // 총 거리 구하기 
    for (int i = 0; i < M; i++)
    {
        int stN  = edges[i].node[0];
        int edN = edges[i].node[1];
        int cost = edges[i].distance;
        if (get_parent(parent, stN) != get_parent(parent, edN))
        {
            union_parent(parent, stN, edN);
            ans += cost;
        }
    }
    cout << ans;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
   freopen("input_c.txt", "r", stdin);

   input();
   solution();
 
    return 0;
}


