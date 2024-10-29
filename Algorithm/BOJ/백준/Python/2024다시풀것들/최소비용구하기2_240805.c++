// https://www.acmicpc.net/problem/11779

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include<queue>
#include<map>
#include <set>
 
#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

// 시작 시간 기준 정렬
// 매 번, 마지막 끝나는 시점 기록
// 매번 길이 계산
// 현재 끝나는 시간 - 이전 마지막 시점 차이 기록해가기 

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    int N, M;
    // 출발, 도착 도시 
    int stCity, edCity;
    // 다익스트라 큐 
    priority_queue<pair<int, int>> queue;
    // 각 정점까지의 거리 
    int distance[MAX];
    fill_n(distance, MAX, INF);
    // 이전 정점
    int lastTrace[MAX];
    fill_n(lastTrace, MAX, -1);
    // 거쳐온 정점 목록
    vector<int> cities;
    // 거쳐온 정점 목록 탐색 idx
    int cIdx = 0;
    // 그래프 
    vector<vector<pair<int,int>>> graph(MAX);
    
    // 입력 ========================
    cin >> N; // 도시 개수 
    cin >> M; // 버스 개수 

    graph.reserve(N+1);
    cities.reserve(N+1);

    for (int i = 0; i < M; i++)
    {
        int  st, ed, cost;
        cin >> st >> ed >> cost;
        graph[st].push_back(make_pair(cost, ed));
    }
    cin >> stCity >> edCity;

    // 다익스트라  =====================
    distance[stCity] = 0;
    queue.push(make_pair(0, stCity));

    while (!queue.empty())
    {
        pair<int, int> c_set = queue.top();
        queue.pop();
        int c_dist = -c_set.first, c_city = c_set.second;
        if (distance[c_city] < c_dist)
            continue;
        for (int i = 0; i < graph[c_city].size(); i++)
        {
            pair<int, int> n_set = graph[c_city][i];

            int n_city = n_set.second;
            int n_dist = c_dist + n_set.first;

            if (n_dist < distance[n_city])
            {
                distance[n_city]  = n_dist;
                lastTrace[n_city] = c_city;
                queue.push(make_pair(-n_dist, n_city));
            }
        }
    }

    cities.push_back(edCity);
    cIdx = edCity;
    lastTrace[stCity] = -1;
    while (lastTrace[cIdx] > 0)
    {
        cities.push_back(lastTrace[cIdx]);
        cIdx = lastTrace[cIdx];
    }

    // update 때마다 도시 개수 + 1
    // 해당 도시 vector에 추가
    cout << distance[edCity] << endl;
    cout << cities.size() << endl;
    for (int i = cities.size() - 1; i >= 0; i--)
        cout << cities[i] << " ";

    return 0; //
}


