# https://www.acmicpc.net/problem/11726

from copy import deepcopy
import heapq as hq
import sys
from functools import reduce
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n = int(input())
dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007
print(dp[n])

# 성공
