# https://www.acmicpc.net/problem/1495

import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

n, s, m = map(int, input().split())
v = [0] + list(map(int, input().split()))
# d[i][j] : i번째 곡을 j 볼륨으로 연주할 수 있느냐
dp = [[-1] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == -1:
            continue
        if j - v[i+1] >= 0:
            dp[i+1][j-v[i+1]] = 1
        if j + v[i+1] <= m:
            dp[i+1][j+v[i+1]] = 1

ans = -1
for i in range(m+1):
    if dp[n][i] == 1:
        ans = i
print(ans)
