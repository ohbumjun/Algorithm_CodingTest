# https://www.acmicpc.net/problem/21608

from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
sits = [[0]*N for _ in range(N)]


def chMostLoves(sits, loves):
    res = []
    maxN = 0
    for r in range(N):
        for c in range(N):
            if sits[r][c] != 0:
                continue
            nums = 0
            for k in range(4):
                nr, nc = r+dx[k], c+dy[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if sits[nr][nc] in loves:
                        nums += 1
            if nums > maxN:
                maxN = nums
                res = []
                res.append((r, c))
            elif nums == maxN:
                res.append((r, c))
    return res


def chMostBlanks(sits, cands):
    res = []
    maxN = 0
    for cand in cands:
        r, c = cand
        if sits[r][c] != 0:
            continue
        nums = 0
        tmps = []
        for k in range(4):
            nr, nc = r+dx[k], c+dy[k]
            if 0 <= nr < N and 0 <= nc < N:
                if sits[nr][nc] == 0:
                    nums += 1
        if nums > maxN:
            maxN = nums
            res = []
            res.append((r, c))
        elif nums == maxN:
            res.append((r, c))
    return res


def calScore(tmp):
    if tmp == 0:
        return 0
    if tmp == 1:
        return 1
    if tmp == 2:
        return 10
    if tmp == 3:
        return 100
    if tmp == 4:
        return 1000


love_d = dict()

for _ in range(N*N):
    nums = list(map(int, input().split()))
    stud = nums[0]
    love = nums[1:]
    love_d[stud] = love
    res = chMostLoves(sits, love)
    if len(res) == 1:
        r, c = res[0]
        sits[r][c] = stud
        continue
    res = chMostBlanks(sits, res)
    if len(res) == 1:
        r, c = res[0]
        sits[r][c] = stud
        continue
    res.sort()
    r, c = res[0]
    sits[r][c] = stud

res = 0
for r in range(N):
    for c in range(N):
        tmp = 0
        for k in range(4):
            nr, nc = r+dx[k], c+dy[k]
            if 0 <= nr < N and 0 <= nc < N:
                if sits[nr][nc] in love_d[sits[r][c]]:
                    tmp += 1
        res += calScore(tmp)
print(res)
