# https://www.acmicpc.net/problem/2457

import itertools
from copy import deepcopy
import heapq
import sys
import math
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000000)

N = int(input())
flws = []

ansSd = 3 * 100 + 1
ansEd = 11 * 100 + 30

for _ in range(N):
    stM, stD, edM, edD = map(int, input().split())
    flws.append((stM*100+stD, edM*100+edD))
flws.sort()

curEd = ansSd
selected = []
changed = False
tmp = -1
x = -1

while curEd <= ansEd and x < N:
    changed = False
    x += 1
    for i in range(x, N):
        if flws[i][0] > curEd:
            break
        if tmp < flws[i][1]:
            tmp = flws[i][1]
            x = i
            changed = True
    if changed:
        curEd = tmp
        selected.append(flws[x])
    else:
        selected = []
        break
    # print("selected",selected)
print(len(selected))
