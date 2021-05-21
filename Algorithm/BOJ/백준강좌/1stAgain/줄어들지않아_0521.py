# https://www.acmicpc.net/problem/2688

# dfs 버전 ------------------------------------
import sys
import heapq
import math
import copy
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


def go(L, idx, tmp):
    global res
    # brute force로 하게 되면, 10^64 가 되버린다
    if L == n:
        res += 1
        ans.append(''.join(map(str, tmp)))
        return
    else:
        for i in range(idx, 10):
            go(L+1, i, tmp+[i])


t = int(input())
for j in range(t):
    n = int(input())
    res = 0
    ans = []
    go(0, 0, [])
    print(res)

# dp 버전 -------------------------------------
# dp[i][j] : i번째 자리에 j가 왔을 때,
# 줄어들지 않는 n자리수 개수

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


t = int(input())
for _ in range(t):
    n = int(input())
    # dp[i][j]
    # i번째 자리에, j가 올때까지, 줄어들지 않는 n자리 수
    dp = [[0]*n for _ in range(10)]
    # 첫행 모두 채우기
    for i in range(n):
        dp[0][i] = 1
    # 첫열 모두 채우기
    for i in range(10):
        dp[i][0] = 1
    for i in range(1, 10):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    sum = 0
    for i in range(10):
        sum += dp[i][n-1]
    print(sum)
