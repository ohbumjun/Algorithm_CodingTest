# https://www.acmicpc.net/problem/3020

import itertools
from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N, H = map(int, input().split())
toUpStones = []  # 석순
toDwStones = []  # 종유석

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        toUpStones.append(h)
    else:
        toDwStones.append(h)

toUpStones.sort()
toDwStones.sort()

minObs = int(1e9)
minScopes = 0


def binSearch(H, stones):
    st = 0
    ed = len(stones)
    hIdx = -1
    while st < ed:
        mid = (st+ed)//2
        if stones[mid] < H:
            st = mid + 1
        else:  # mid >= H
            hIdx = mid
            ed = mid
    hIdx = len(stones) if hIdx == -1 else hIdx
    return len(stones) - hIdx


for h in range(1, H+1):  # i : 구간의 높이
    obs1 = binSearch(h, toUpStones)  # 석순 장애물 개수
    obs2 = binSearch((H+1)-h, toDwStones)  # 종유석 장애물 개수
    nObs = obs1 + obs2  # 둘의 합
    # 핵심 : 선형 탐색을 하면, 시간 초과! 따라서 이분탐
    if minObs == nObs:
        minScopes += 1
    elif minObs > nObs:
        minObs = nObs
        minScopes = 1

print(minObs, minScopes)
