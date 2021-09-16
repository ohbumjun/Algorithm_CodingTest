# https://www.acmicpc.net/problem/10026

import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
우선, 일반적으로 그냥 구역을 구하는 경우의 수를 살펴보자

2차원으로 쭉 돈다.

아직 방문하지 않은 정점이 있다면 res에 1을 더해주고 
거기서부터 bfs를 시작한다
다른 점이 나올때까지 반복하는데
방문할때마다 check 표시 

'''
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
arr = [list(input()) for _ in range(n)]
chk = [[0] * n for _ in range(n)]
res = 0

# 적록색 아닌 사람
for i in range(n):
    for j in range(n):
        if chk[i][j] == 0:
            res += 1
            chk[i][j] = 1
            val = arr[i][j]
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or n <= nx or ny < 0 or n <= ny:
                        continue
                    if arr[nx][ny] != val or chk[nx][ny] != 0:
                        continue
                    chk[nx][ny] = 1
                    q.append((nx, ny))
print(res, end=' ')

# 적록색인 사람
chk = [[0] * n for _ in range(n)]
res = 0
for i in range(n):
    for j in range(n):
        if chk[i][j] == 0 and arr[i][j] == 'B':
            res += 1
            chk[i][j] = 1
            val = arr[i][j]
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or n <= nx or ny < 0 or n <= ny:
                        continue
                    if arr[nx][ny] != val or chk[nx][ny] != 0:
                        continue
                    chk[nx][ny] = 1
                    q.append((nx, ny))
        elif chk[i][j] == 0:
            res += 1
            chk[i][j] = 1
            val = arr[i][j]
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or n <= nx or ny < 0 or n <= ny:
                        continue
                    if arr[nx][ny] == 'B' or chk[nx][ny] != 0:
                        continue
                    chk[nx][ny] = 1
                    q.append((nx, ny))
print(res, end=' ')
