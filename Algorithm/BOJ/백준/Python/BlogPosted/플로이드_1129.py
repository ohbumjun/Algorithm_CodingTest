# https://www.acmicpc.net/problem/11404

import sys
import heapq
from copy import deepcopy
from collections import Counter , deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)
 
# 모든 점에서, 다른 모든점까지의 최소 거리 = 플로이드 와샬
n = int(input())
m = int(input())

INT_MAX = int(1e9)
dp     = [[INT_MAX] * n for _ in range(n)]

# 자기 자신으로의 거리 0
for i in range(n):
    dp[i][i] = 0
    
for _ in range(m):
    st,ed,cst  = map(int,input().split())
    st,ed      = st-1,ed-1
    if cst < dp[st][ed] : 
        dp[st][ed] = cst

# 플로이드 와샬을 이용해서, 한 도시에서 다른 도시로 가는 비용 계산
for k in range(n):
    for r in range(n):
        for c in range(n):
            dp[r][c] = min(dp[r][c] , dp[r][k] + dp[k][c])
                

# 경로없는 경우 비용 0으로
for r in range(n):
    for c in range(n):
        if dp[r][c] == INT_MAX :
            dp[r][c] = 0
# print()
for d in dp : print(' '.join(map(str,d)))


