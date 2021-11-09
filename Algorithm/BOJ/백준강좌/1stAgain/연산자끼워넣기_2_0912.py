from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
1[]2[]3[]4[]5[]6
- 
'''
# 계산은 무조건 앞에서부터
# 나눗셈은 정수 나눗셈으로 몫만 취하기
# 음수를 양수로 나눌 땐, 양수로 나눈 다음 목을 양수로
# 각 연산자에 해당하는, 숫자를 세팅 --> 비트마스크로 구해간다

N = int(input())
A = list(map(int, input().split()))
p, m, mp, dv = map(int, input().split())
c_arr = ['a' for i in range(p)] + ['b' for i in range(m)] + \
    ['c' for i in range(mp)] + ['d' for i in range(dv)]
l_c = len(c_arr)
l_A = len(A)
res = []


def cal(ans, c, val):
    if c == 'a':
        return ans + val
    if c == 'b':
        return ans - val
    if c == 'c':
        return ans * val
    if c == 'd':
        if ans < 0:
            return -((-ans) // val)
        else:
            return ans // val


def go(p_n, p_m, p_mp, p_dv, idx, ans):
    global minV, maxV
    if idx == l_A - 1:
        res.append(ans)
        return
    if p_n > 0:
        go(p_n-1, p_m, p_mp, p_dv, idx+1, cal(ans, 'a', A[idx+1]))
    if p_m > 0:
        go(p_n, p_m-1, p_mp, p_dv, idx+1, cal(ans, 'b', A[idx+1]))
    if p_mp > 0:
        go(p_n, p_m, p_mp-1, p_dv, idx+1, cal(ans, 'c', A[idx+1]))
    if p_dv > 0:
        go(p_n, p_m, p_mp, p_dv-1, idx+1, cal(ans, 'd', A[idx+1]))


go(p, m, mp, dv, 0, A[0])
res.sort()
print(res[-1])
print(res[0])
