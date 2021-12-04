#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include <algorithm>
#include<queue>
 
#define endl "\n"

// 상수
#define NODE_MAX 20000 + 1
#define EDGE_MAX 300000 + 1
#define INF 1e9

using namespace std;
// visited
bool visited[NODE_MAX];
// distance
int dist[NODE_MAX];
// graph
vector<pair<int, int>> graph[NODE_MAX];
// 정점, 간선
int V, E, start;

void input()
{
    // distance 무한대로 초기화 
    fill_n(dist, NODE_MAX, INF);
    // visited 모두 false
    fill_n(visited, NODE_MAX, false);

    cin >> V >> E;
    cin >> start;
    for (int i = 0; i < E; i++)
    {
        int st, ed, cost;
        cin >> st >> ed >> cost;
        graph[st].push_back(make_pair(ed,cost));
    }
}

int get_smallest_node()
{
    int min_value = INF - 1;
    int min_idx    = -1;
    for (int i = 1; i <= V; i++)
        cout << dist[i] << ". ";
    cout << endl;
    for (int i = 1; i <= V; i++)
        cout << visited[i] << ". ";
    cout << endl;
    cout << endl;
    for (int i = 1; i <= V; i++)
    {
        if (visited[i] == false && dist[i] <= min_value)
        {
            min_value = dist[i];
            min_idx = i;
        }
    }
    return min_idx;
}

void dijkstra(int start_node)
{
    // startNode로 초기화
    visited[start_node] = true;
    dist[start_node] = 0;

    // 최초 dist 정보 초기화
    for (int i = 0; i < graph[start_node].size(); i++)
    {
        int nxt_node = graph[start_node][i].first;
        dist[nxt_node] = graph[start_node][i].second;
    }
    
    // V - 1 개의 정점 선택해가기
    for (int i = 0; i < V - 1; i++)
    {
        int now = get_smallest_node();

        // 이 예외는, 더이상, 
        // 1) 방문하지 않은 노드 중에서
        // 2) 갈 수 있는 노드가 없을 때
        // 3) 위에 get_smallest_node의 minIdx 변수가 update 안되서
        // -1로 그대로 넘어온다
        if (now == -1)
            continue;
        visited[now] = true;
        
        int edge_size = graph[now].size();
       //  cout << "edge_size : " << edge_size << endl;
        for (int j = 0; j < graph[now].size(); j++)
        {
            int nxt_node = graph[now][j].first;
            int nxt_cost = dist[now] + graph[now][j].second;

            if (dist[nxt_node] > nxt_cost)
                dist[nxt_node] = nxt_cost;
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
   freopen("input_C.txt", "r", stdin);

   input();
   dijkstra(start);
   for (int i = 1; i <= V; i++)
   {
       if (dist[i] == INF)
           cout << "INF" << endl;
       else
           cout << dist[i] << endl;
   }
 
    return 0;
}


