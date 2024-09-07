# https://www.acmicpc.net/problem/9095
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

n = int(input())
m = 3
nums = [1, 2, 3]
dp = [0]*11
dp[0] = 1
for i in range(len(dp)):
    for j in range(m):
        if i - nums[j] >= 0:
            dp[i] += dp[i-nums[j]]
print("dp", dp)
