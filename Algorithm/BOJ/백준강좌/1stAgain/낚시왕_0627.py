#

# 첫번째 풀이 : 메모리 초과
from copy import deepcopy
import heapq as hq
import sys
from functools import reduce
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1501*1501)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 배열
ans = 0
R, C, m = map(int, input().split())
speed = [0]*(m+1)  # 속력
dirs = [0]*(m+1)  # 이동 방향
shark = [[(-1, -1)]*C for _ in range(R)]  # (번째,크기)
shark_next = [[0]*C for _ in range(R)]
temp = [list(map(int, input().split())) for _ in range(m)]
for t in range(m):
    r, c, s, d, z = temp[t]
    # 상어 정보
    shark[r-1][c-1] = (t+1, z)
    dirs[t+1] = d-1
    speed[t+1] = s


def opp(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    return 2


def catch_shark(c):
    global ans
    for i in range(R):
        if shark[i][c] != (-1, -1):
            ans += shark[i][c][1]
            shark[i][c] = (-1, -1)
            break


def move_shark():
    # shark_next 초기화
    v = []
    for i in range(R):
        for j in range(C):
            # 번째, 크기
            shark_next[i][j] = (-1, -1)
            if shark[i][j][0] > 0:
                idx, size = shark[i][j]
                # 크기,속력,방향
                v.append((idx, size, i, j))
    for e in v:
        idx, size, x, y = e
        sp, direc = speed[idx], dirs[idx]
        # 이동 처리
        fx, fy = x, y
        for i in range(sp):
            nx, ny = fx+dx[direc], fy+dy[direc]
            if 0 <= nx < R and 0 <= ny < C:
                fx, fy = nx, ny
            else:
                # 방향 전환
                direc = opp(direc)
                dirs[idx] = direc
                fx, fy = fx+dx[direc], fy+dy[direc]
        # fx,fy에 최종 이동 위치 세팅
        if shark_next[fx][fy] == (-1, -1):
            shark_next[fx][fy] = (idx, size)
        else:
            if shark_next[fx][fy][1] < size:
                shark_next[fx][fy] = (idx, size)
    # 이제 shark_next 정보 --> shark 복사하기
    for i in range(R):
        for j in range(C):
            shark[i][j] = shark_next[i][j]


for c in range(C):
    catch_shark(c)
    move_shark()
print(ans)
