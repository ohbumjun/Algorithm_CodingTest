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
        parent[px] = py; //
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
    // 굳이 2개의 반복문을 돌 필요가 없다
    // 크루스칼은, 단순히, 모든 정점을 연결만 해주면 되기 때문에
    // 간선의 비용이 적은 순서대로, 선택해가기만 하면 된다.
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
    cout << ans; //
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
   freopen("input_c.txt", "r", stdin);

   input();
   solution(); //
 
    return 0;
}

// Prim 알고리즘
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
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int Graph[MAX][MAX] = {INF,};

// i번째 정점과 가장 가까운 정점
int vecNearest[MAX];

// 최소 비용 신장 트리 에서 해당 정점까지의 최단 거리
// (최소 비용 신장 트리에 속하는 정점들은 -1 값)
int vecDist[MAX];

int N, M;

void Input()
{
    cin >> N >> M;

    for (int r = 1; r <= N; ++r)
        for (int c = 1; c <= N; ++c)
            Graph[r][c] = INF;

    for (int i = 0; i < M; ++i)
    {
        int st, ed, cost;
        cin >> st >> ed >> cost;
        Graph[st][ed] = cost;
        Graph[ed][st] = cost;
    }
    
}

void Solve()
{
    memset(vecNearest, INF, sizeof(vecNearest));

    for (int i = 0; i <= N; ++i)
        vecDist[i] = INF;

	// 1번째 정점을 포함시킨 이후 진행
    int Answer = 0;

    vecDist[1] = -1;

    // for (int i = 1; i <= N; ++i)
    // {
    //     for (int c = 1; c <= N; ++c)
    //     {
    //         cout << Graph[i][c] << ".";
    //     }
    //     cout << endl;
    // }

 
    for (int i = 2; i <= N; ++i)
    {
	    if (Graph[1][i] != INF) // 1번째 정점과 연결된 녀석이라면 
	    {
            vecNearest[i] = 1;
            vecDist[i] = Graph[1][i];
	    }
    }


    // 이후 N - 1 개의 정점을 추가로 포함시키면 된다.
    for (int i = 0; i < N - 1; ++i)
    {
        int minDist = INF, minNode = -1;


        // 모든 정점 중에서, 최소 비용에 속하지 않으면서, 가장 가까운 거리에 있는 정점들을 선택해간다.
	    for (int t = 2; t <= N; ++t)
	    {
		    if (vecDist[t] != -1 && vecDist[t] < minDist)
		    {
                minDist = vecDist[t], minNode = t;
		    }
	    }

        vecDist[minNode] = -1;

   
        Answer += minDist;

        // 선택된 노드를 기준으로 최소 비용 정보를 Update
        for (int t = 2; t <= N; ++t)
        {
            // 최소 비용에 속하지 않은 노드들에 대해서 
	        if (vecDist[t] > Graph[minNode][t])
	        {
                vecDist[t] = Graph[minNode][t];
                vecNearest[t] = minNode;
	        }
        }
    }

    cout << Answer << endl;
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