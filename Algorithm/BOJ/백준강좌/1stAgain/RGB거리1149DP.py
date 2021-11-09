# https://www.acmicpc.net/problem/1149

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

n = int(input())

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

    '''
    p[i][0] : i번째 집을 빨강으로 칠했을 때, 지금까지의 집 칠하는 최소 비용
    p[i][1] : i번째 집을 파랑으로 칠했을 때, 지금까지의 집 칠하는 최소 비용
    p[i][2] : i번째 집을 그린으로 칠했을 때, 지금까지의 집 칠하는 최소 비용
    
    '''

for i in range(1, len(p) ):
    p[i][0] = min( p[i-1][1], p[i-1][2] ) + p[i][0]
    p[i][1] = min( p[i-1][0], p[i-1][2] ) + p[i][1]
    p[i][2] = min( p[i-1][0], p[i-1][1] ) + p[i][2]

print(min(p[n-1][0], p[n-1][1], p[n-1][2]))
            

    
