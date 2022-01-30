# https://www.acmicpc.net/problem/17144

import sys
import heapq
import math
import copy
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dx = [0, -1, 0, 1]  # 오,위,왼,아
dy = [1, 0, -1, 0]  # 오,위,왼,아

R, C, T = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(R)]


def go(sx, sy, z):
    k = 0
    q = deque()
    cx = sx + dx[k]
    cy = sy + dy[k]
    air_sp[cx][cy] = 0
    q.append((cx, cy))
    # 우선 해당 방향대로 이동시킨다
    while q:
        x, y = q.popleft()
        if x == sx and y == sy:
            break
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 > nx or nx >= R or 0 > ny or ny >= C:
            # 해당 방향이 범위를 벗어나면, 방향을 바꾼다
            nx -= dx[k]
            ny -= dy[k]
            k = (k + z) % 4
            nx += dx[k]
            ny += dy[k]
        # break 되는 것은 아닌가 ?
        air_sp[nx][ny] = a[x][y]
        a[x][y] = 0
        q.append((nx, ny))
    # 확산된 내용을 반영해야 한다( 이렇게 해주는 이유는 "동시에" 퍼지는 것을 제대로 반영하기 위해 )
    for i in range(R):
        for j in range(C):
            if a[i][j] == -1:
                continue
            if air_sp[i][j] != 0:
                a[i][j] = air_sp[i][j]
                air_sp[i][j] = 0


# 공기청정기 위치를 찾는다
up_c, down_c = -1, -1
for i in range(R):
    for j in range(C):
        if a[i][j] == -1:
            if up_c == -1:
                up_c = (i, j)
            else:
                down_c = (i, j)

for _ in range(T):
    mise_sp = [[0]*C for _ in range(R)]
    air_sp = [[0]*C for _ in range(R)]

    # 미세먼지 확산을 계산
    for i in range(R):
        for j in range(C):
            if a[i][j] not in [0, -1]:
                spN = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if a[nx][ny] != -1:
                            mise_sp[nx][ny] += (a[i][j]//5)
                            spN += 1
                a[i][j] -= ((a[i][j]//5) * spN)

    # 확산된 양을, 다시 더한다
    for i in range(R):
        for j in range(C):
            a[i][j] += mise_sp[i][j]

    # 위쪽 공기청정기
    go(up_c[0], up_c[1], 1)
    # 아래쪽 공기청정기
    go(down_c[0], down_c[1], 3)

res = 0
for i in range(R):
    for j in range(C):
        res += a[i][j]
print(res + 2)  # +2 를 해주는 이유는, 공기청정기에 해당하는 -1을 2번 더해줬기 때문이다
