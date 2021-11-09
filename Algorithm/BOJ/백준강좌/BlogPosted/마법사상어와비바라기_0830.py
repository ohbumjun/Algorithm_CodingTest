# https://www.acmicpc.net/problem/21610

from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(100000)

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dxx = [-1, -1, 1, 1]
dyy = [-1, 1, -1, 1]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
groom = deque([(N-1, 0), (N-2, 0), (N-1, 1), (N-2, 1)])

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    # 1) 해당 방향으로 구름 이동 처리
    for _ in range(s):
        n_groom = deque()
        while groom:
            cx, cy = groom.popleft()
            nx, ny = cx+dx[d], cy+dy[d]
            # 행 처리
            if nx < 0:
                nx = N-1
            nx = nx % N
            # 열 처리
            if ny < 0:
                ny = N-1
            ny = ny % N
            n_groom.append((nx, ny))
        # 새로운 구름 위치
        groom = n_groom
    # 구름 이동 완료
    # 2) 해당 위치의 바구니 물의 양 1 증가 + 구름 소멸
    busket = deque()
    disappear = []
    while groom:
        cx, cy = groom.popleft()
        maps[cx][cy] += 1
        # 물이 증가한 위치목록 추가
        busket.append((cx, cy))
        disappear.append((cx, cy))
    # 3) 물복사 버그
    while busket:
        cx, cy = busket.popleft()
        s = 0
        # 대각선 방향 이동
        for k in range(4):
            nx, ny = cx+dxx[k], cy+dyy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if maps[nx][ny] > 0:
                s += 1
        maps[cx][cy] += s
    # 4) 새로운 구름 생성
    for r in range(N):
        for c in range(N):
            if maps[r][c] >= 2 and (r, c) not in disappear:
                groom.append((r, c))
                maps[r][c] -= 2
res = 0
for r in range(N):
    for c in range(N):
        res += maps[r][c]
print(res)
