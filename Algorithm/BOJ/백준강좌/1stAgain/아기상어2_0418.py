# https://www.acmicpc.net/problem/17086

# 첫번째 혼자 풀이 ----
'''
모든 아기 상어를 조사
- 각 아기상어 에서의 거리를 조사하면 되는 것이 아닌가 ??
- 각 아기상어에서 bfs를 매번 새롭게 실시하면 되는 것이 아닌가 ??

'''
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

# 8 방향
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

n, m = map(int, input().split())  # n,m : 행, 열
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

# 모든 위치에 대해서, bfs를 실시하고, 거기에서의 최대값을 구한다


def go(i, j):
    dist = [[-1]*m for _ in range(n)]
    minD = -1
    q = deque()
    q.append((i, j))
    dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    minD = dist[x][y] + 1

                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    res = max(res, minD)


print(res)
