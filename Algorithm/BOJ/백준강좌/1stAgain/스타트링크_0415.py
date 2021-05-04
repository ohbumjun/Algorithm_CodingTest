# https://www.acmicpc.net/problem/5014

# 처음 풀이 --------------------------------------------------
'''
틀린 이유 

if 0 <= now - D < F+1 and chk[now-D] == -1:
        chk[now-D] = 1
        dist[now-D] = dist[now] + 1
        q.append(now-D)

에서 최소범위가 0이 아니라, 1이 되어야 한다  

if 1 <= now - D < F+1 and chk[now-D] == -1:
        chk[now-D] = 1
        dist[now-D] = dist[now] + 1
        q.append(now-D)

'''
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)


'''
F : 총 층 건물수 --> 총 건물 dist 배열 개수
S, G

U : 위층으로 --> 간선 가중치는 동일 이동하는 경로
D : 아래층으로 
'''

F, S, G, U, D = map(int, input().split())

dist = [-1] * (F+1)
chk = [-1] * (F+1)

dist[S] = 0
chk[S] = 1
q = deque()
q.append(S)

while q:
    now = q.popleft()

    if 0 <= now + U < F+1 and chk[now+U] == -1:
        chk[now+U] = 1
        dist[now+U] = dist[now] + 1
        q.append(now+U)
    if 0 <= now - D < F+1 and chk[now-D] == -1:
        chk[now-D] = 1
        dist[now-D] = dist[now] + 1
        q.append(now-D)

print(dist[G] if dist[G] != -1 else 'use the stairs')

# 문제 해설
'''
엘리베이터 각 층이 정점
한층에서, 다른 층으로 가는 것이 간선

총 정점의 개수는, 건물의 높이
층간의 최소 이동 횟수를 구하는 문제이므로, BFS

'''
F, S, G, U, D = map(int, input().split())

dist = [-1] * (F+1)
chk = [-1] * (F+1)

dist[S] = 0
chk[S] = 1
q = deque()
q.append(S)

while q:
    now = q.popleft()

    if 1 <= now + U < F+1 and chk[now+U] == -1:
        chk[now+U] = 1
        dist[now+U] = dist[now] + 1
        q.append(now+U)
    if 1 <= now - D < F+1 and chk[now-D] == -1:
        chk[now-D] = 1
        dist[now-D] = dist[now] + 1
        q.append(now-D)

print(dist[G] if dist[G] != -1 else 'use the stairs')

# C++
'''
#include <iostream>
#include <queue>
using namespace std;
int dist[1000001];
bool check[1000001];
int main() {
    int f,s,g,u,d;
    cin >> f >> s >> g >> u >> d;
    queue<int> q;
    q.push(s);
    check[s] = true;
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        if (now + u <= f && check[now+u] == false) {
            dist[now+u] = dist[now] + 1;
            check[now+u] = true;
            q.push(now+u);
        }
        if (now - d >= 1 && check[now-d] == false) {
            dist[now-d] = dist[now] + 1;
            check[now-d] = true;
            q.push(now-d);
        }
    }
    if (check[g]) {
        cout << dist[g] << '\n';
    } else {
        cout << "use the stairs\n";
    }
    return 0;
}
'''
