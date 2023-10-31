# https://www.acmicpc.net/problem/1167

from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100001)
#

# bfs : 임의의 한점에서 가장 먼점과 그 거리를 리턴하는 함수


def bfs(num):
    maxDist, node = 0, num
    queue = deque()
    queue.append((num, 0))
    ch[num] = 1

    while queue:
        q = queue.popleft() #
        print("q", q)
        nowDist = q[1]
        nowNode = q[0]

        for n in adj[nowNode]:
            if ch[n[0]] == 0:
                ch[n[0]] = 1
                print("append", (n[0], nowDist + n[1]))
                queue.append((n[0], nowDist + n[1]))
                if maxDist < nowDist + n[1]:
                    maxDist = nowDist + n[1]
                    node = n[0]

    return node, maxDist


# 인접리스트 생성
n = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp) - 1, 2):
        adj[tmp[0]].append((tmp[j], tmp[j+1]))

N, D = bfs(1)

# 체크리스트 초기화
for i in range(len(ch)):
    ch[i] = 0
print("N", D)
print(bfs(N)[1])


'''
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <math.h>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)

using namespace std;

int V;
vector<vector<pair<int, int>>> vecGraph;
vector<bool> vecCheck;
vector<int>   vecDist;

int maxDistToLast = 0;
int maxLastNode = -1;

void Input()
{
    cin >> V;

    vecGraph.resize(V + 1);
    vecDist = vector<int>(V + 1, INT_MAX);
    vecCheck = vector<bool>(V + 1, false);

    for (int v = 0; v < V; ++v)
    {
        int st;
        cin >> st;
        while (true)
        {
            int nxt, cost;
            cin >> nxt;
            if (nxt == -1)
                break;
            cin >> cost;
            vecGraph[st].push_back(make_pair(nxt, cost));
            vecGraph[nxt].push_back(make_pair(st, cost));
        }
    }
};

void Dijkstra(int stNode)
{
    // curNode, accDist
    priority_queue<pair<int, int>> Queue;
    Queue.push(make_pair(stNode, 0));
    vecCheck[stNode] = 0;

    while (!Queue.empty())
    {
        auto [curNode, accDist] = Queue.top();
        Queue.pop();

        if (vecDist[curNode] < accDist)
            continue;

        vecDist[curNode] = accDist;

        if (vecCheck[curNode])
            continue;

        vecCheck[curNode] = true;

        for (int i = 0; i < vecGraph[curNode].size(); ++i)
        {
            int nxtN = vecGraph[curNode][i].first;
            int nDist = vecGraph[curNode][i].second;

            if (vecCheck[nxtN])
                continue;

            Queue.push(make_pair(nxtN, accDist + nDist));
        }
    }
};

void Solve()
{
    Dijkstra(1);

    for (int i = 1; i <= V; ++i)
    {
        if (vecDist[i] > maxDistToLast)
        {
            maxDistToLast = vecDist[i];
            maxLastNode = i;
        }
    }

    // cout << "maxDistToLast, maxLastNode : " << maxDistToLast << "," << maxLastNode << endl;

    vecDist = vector<int>(V + 1, INT_MAX);
    vecCheck = vector<bool>(V + 1, false);

    Dijkstra(maxLastNode);

    maxDistToLast = 0;
    maxLastNode = -1;

    for (int i = 1; i <= V; ++i)
    {
        if (vecDist[i] > maxDistToLast)
        {
            maxDistToLast = vecDist[i];
            maxLastNode = i;
        }
    }

    // cout << "maxDistToLast, maxLastNode : " << maxDistToLast << "," << maxLastNode << endl;

    cout << maxDistToLast << endl;
};

int main() {
    ios::sync_with_stdio(false);

    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();

    Solve();
    
    return 0;
}


'''