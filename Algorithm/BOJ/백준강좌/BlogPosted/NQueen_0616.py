# 최적화 x 코드 ---
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n = int(input())
ch = [[-1]*n for _ in range(n)]
ans = 0

'''
한칸씩 내려가면서
1) 같은 열에 있는지 검사
2) 대각선에 있는지 검사
3) 마지막에 오면, cnt에 1 더해주기 
'''


def check(row, col):
    # 세로 행 검사
    for r in range(row):
        if ch[r][col] != -1:
            return False
    # 왼쪽 대각선 검사
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if ch[i][j] != -1:
            return False
        i -= 1
        j -= 1
    # 오른쪽 대각선 검사
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if ch[i][j] != -1:
            return False
        i -= 1
        j += 1
    return True

    return


def go(row):
    global ans
    if row == n:
        ans += 1
        return
    else:
        for i in range(n):
            if check(row, i):
                # 현재를 검사하는건가 아니면
                # 그 다음 row를 검사하는 건가
                ch[row][i] = 1
                go(row+1)
                ch[row][i] = -1


go(0)
print(ans)

# 최적화 코드 ---


def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True


def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row, col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans


n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))
