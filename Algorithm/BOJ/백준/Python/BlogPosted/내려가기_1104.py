# https://www.acmicpc.net/problem/2096

import sys

# 핵심 : dp 배열, 기존 정보 저장 배열 둘다 만들지 말기!

N = int(input())
dpMx = [0]*3
dpMn = [0]*3
dpMx_c = [0]*3
dpMn_c = [0]*3

for i in range(N):
    a, b, d = map(int, sys.stdin.readline().split())
    for c in range(3):
        if c == 0:
            dpMx_c[c] = a + max(dpMx[c], dpMx[c+1])
            dpMn_c[c] = a + min(dpMn[c], dpMn[c+1])
        if c == 1:
            dpMx_c[c] = b + max(dpMx)
            dpMn_c[c] = b + min(dpMn)
        if c == 2:
            dpMx_c[c] = d + max(dpMx[c], dpMx[c-1])
            dpMn_c[c] = d + min(dpMn[c], dpMn[c-1])
    for i in range(3):
        dpMx[i] = dpMx_c[i]
        dpMn[i] = dpMn_c[i]

print(max(dpMx))
print(min(dpMn))
