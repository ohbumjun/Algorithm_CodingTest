# https://www.acmicpc.net/problem/14442

import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
벽 부수고 이동하기

빈칸 > 빈칸 : 무조건 가능 
빈칸 > 벽 : z가 k개보다 작으면 가능 
벽 > 빈칸 : 무조건 가능 
벽> 벽 : z가 k개보다 작으면 가능

1) 모든 정점에 대해 해당 함수 실행 => Brute Force //
2) dfs : 모든 정점까지의 거리를 저장하는 배열 
- dist라는 3차원 배열 : 이미 방문했으면 안간다

즉, 벽 부수고 이동하기1 에다가
벽을 부술 수 있는 개수가 더 많아진 것이고

그저 K개라는 벽을 기준으로
z == 0 이 아니라 
z < K 일때까지 반복할 수 있게 되는 것이다

'''

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 따라서 출발점도 dist 상으로 1이 되는 것이다
dist[0][0][0] = 1
queue = deque([(0, 0, 0)])
while queue:
    x, y, z = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 빈칸, 빈칸 // 벽 , 빈칸
            if arr[nx][ny] == 0 and dist[nx][ny][z] == 0:
                queue.append((nx, ny, z))
                dist[nx][ny][z] = dist[x][y][z] + 1
            # 빈칸 > 벽 , 벽 > 벽
            # z 범위가 z == K 까지는 되야 한다. 왜냐하면 z == K라는 것은 K개의 벽을 깼다는 것이므로
            if z < K and arr[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                queue.append((nx, ny, z+1))
                dist[nx][ny][z+1] = dist[x][y][z] + 1

res = -1

for i in range(K+1):
    if dist[N-1][M-1][i] == 0:
        continue
    if res == -1:
        res = dist[N-1][M-1][i]
    elif res > dist[N-1][M-1][i]:
        res = dist[N-1][M-1][i]

print(res)


# C++ 코드 -------------------------------
# include <iostream>
# include <queue>
# include <cstdio>
# include <tuple>
# include <cstring>
using namespace std
int a[1000][1000]
int d[1000][1000][11]
int dx[] = {0, 0, 1, -1}
int dy[] = {1, -1, 0, 0}
int main() {
    int n, m, l
    scanf("%d %d %d", & n, & m, & l)
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < m
             j++) {
            scanf("%1d", & a[i][j])
        }
    }
    queue < tuple < int, int, int >> q
    d[0][0][0] = 1
    q.push(make_tuple(0, 0, 0))
    while (!q.empty()) {
        int x, y, z
        tie(x, y, z) = q.front()
        q.pop()
        for (int k=0
             k < 4
             k++) {
            int nx = x+dx[k]
            int ny = y+dy[k]
            if (nx < 0 | | nx >= n | | ny < 0 | | ny >= m) continue
            if (a[nx][ny] == 0 & & d[nx][ny][z] == 0) {
                d[nx][ny][z] = d[x][y][z] + 1
                q.push(make_tuple(nx, ny, z))
            }
            if (z+1 <= l & & a[nx][ny] == 1 & & d[nx][ny][z+1] == 0) {
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.push(make_tuple(nx, ny, z+1))
            }
        }
    }
    int ans = -1
    for (int i=0
         i <= l
         i++) {
        if (d[n-1][m-1][i] == 0) continue
        if (ans == -1) {
            ans = d[n-1][m-1][i]
        } else if (ans > d[n-1][m-1][i]) {
            ans = d[n-1][m-1][i]
        }
    }
    cout << ans << '\n'
    return 0; //
}
