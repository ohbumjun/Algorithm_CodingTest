#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include <algorithm>
#include <functional>
#include<queue>
 
#define endl "\n"
#define NODE_MAX 20000 + 1
#define EDGE_MAX 300000 + 1
#define INF int(1e9)


using namespace std;

int V, E, start_node;
vector<pair<int, int>> graph[NODE_MAX];
int   dist[NODE_MAX];

void input()
{
    cin >> V >> E;
    cin >> start_node;
    for (int i = 0; i < E; i++)
    {
        int stN, edN, cst;
        cin >> stN >> edN >> cst;
        graph[stN].push_back(make_pair(edN, cst));
    }

    // 초기화
    fill_n(dist, NODE_MAX, INF);
}


void dijkstra(int start)
{
    priority_queue<pair<int, int>> pq;

    dist[start] = 0;
    pq.push({ 0, start });
    
    while (!pq.empty())
    {
        int cur_node      = pq.top().second;
        int dist_to_node = -pq.top().first;
        pq.pop();
        // 이미 방문 처리된 노드라면 skip
        if (dist_to_node > dist[cur_node])
            continue;
        // 주변 정보 update 
        int edge_size = graph[cur_node].size();
        for (int i = 0; i < edge_size; i++)
        {
            int nxt_node = graph[cur_node][i].first;
            int nxt_cost  = dist[cur_node] + graph[cur_node][i].second;
            if (nxt_cost < dist[nxt_node])
            {
                dist[nxt_node] = nxt_cost;
                pq.push({ -nxt_cost , nxt_node });
            }
        }
    }
}

void solve()
{
    dijkstra(start_node);
    for (int i = 1; i <= V; i++)
    {
        if (dist[i] == INF)
            cout << "INF" << endl;
        else
            cout << dist[i] << endl;
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
   freopen("input_C.txt", "r", stdin); //

   input();
   solve();
 
    return 0;
}


