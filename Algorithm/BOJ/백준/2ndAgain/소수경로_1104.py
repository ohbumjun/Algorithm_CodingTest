# https://www.acmicpc.net/problem/1963

import sys
import heapq
import math
from collections import deque
sys.setrecursionlimit(100000)


def nextNum(num, idx, newN):
    if idx == 0 and newN == 0:
        return -1
    num = list(str(num))
    num[idx] = newN
    num = ''.join(map(str, num))
    return int(num)


prime = [True] * 10001
# 소수 세팅
for i in range(2, 10001):
    if prime[i] == True:
        for j in range(i+i, 10001, i):
            if j <= 10000:
                prime[j] = False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(0)
        continue
    # BFS를 위한 distance, Check 배열 초기화
    INT_MAX = int(1e9)
    d = [INT_MAX] * 10001
    d[n] = 0
    q = deque([n])
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = nextNum(now, i, j)
                if nxt != -1:
                    if prime[nxt] == True and d[nxt] > d[now] + 1:
                        d[nxt] = d[now] + 1
                        q.append(nxt)
    print(d[m])
