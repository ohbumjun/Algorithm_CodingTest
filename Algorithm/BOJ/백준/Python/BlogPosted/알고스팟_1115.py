# https://www.acmicpc.net/problem/1261

import sys
import heapq
from collections import Counter , deque
sys.setrecursionlimit(100000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N     = map(int,input().split())
mirrors = [list(map(int,input())) for _ in range(N)]
dist     = [[-1] * M for _ in range(N)]

q             = deque()
dist[0][0] = 0
q.append((0,0,0))

ans = int(1e9)

while q :
    x,y,d = q.popleft()
    if x == N-1 and y == M -1 :
        ans = min(ans,d)
        continue
    for k in range(4) :
        nx,ny = x + dx[k] , y + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if dist[nx][ny] != -1 and dist[nx][ny] <= d + mirrors[nx][ny] : continue
            dist[nx][ny] = d + mirrors[nx][ny]
            q.append((nx,ny,dist[nx][ny]))
print(dist[N-1][M-1])

