# https://www.acmicpc.net/problem/14465

import itertools
from copy import deepcopy
import heapq
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N, K, B = map(int, input().split())
light = [True]*N
for _ in range(B):
    light[int(input())-1] = False

ans = -1

for i in range(N-K+1):  # 4 ( 0 ~ 3 )
    nF = 0
    for j in range(i, i+K):  # 3 ~ 9
        if not light[j]:
            nF += 1
    if ans == -1 or nF < ans:
        ans = nF
print(ans if ans != -1 else 0)
