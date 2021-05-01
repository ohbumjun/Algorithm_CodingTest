# https://www.acmicpc.net/problem/1495

import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)
'''
0 1 2 3 4 5 6 7 8
0 2 4 6 8  ...

즉, n개의 곡을 연주하기 위해서
곡을 2^n 번 바꿀 수 있다는 것이다

100개를 다 조사하면 시간초과

우리가 관심있는 것은 사실
어떤 곡에서, 어떤 볼륨으로 연주될 수 있는지이다

d[i][j] : i번째 곡에서 j번째 volume 으로 연주될 수 있는가 ??
- 0 : no
- 1 : yes

'''
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
