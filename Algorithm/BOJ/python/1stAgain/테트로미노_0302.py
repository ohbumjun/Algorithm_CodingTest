# https://www.acmicpc.net/problem/14500

# 첫번째 풀이 : Brute Force
import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
ch = [[0] * m for _ in range(n)]
dCol = [-1, 0, 1, 0]
dRow = [0, -1, 0, 1]
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# x, y 좌표
# sum : 지금까지 간 간격에 있던 수들의 합
# cnt : 몇칸 갔는지 ( 4칸까지 ! )


'''
4가지 경우를 제외하고는 사실
연속적으로 3번을 움직이는 과정이다
'''


def go(x, y, sum, cnt):
    global ans
    if cnt == 4:
        if sum > ans:
            ans = sum

    # 이미 방문처리되었다면 or 범위를 벗어난다면
    if (x <= 0 or x >= n or y <= 0 or y >= m):
        return
    if (ch[x][y] == 1):
        return

    # 방문 처리 ( 다시해당 칸으로 돌아가지 않게 하기 위해서
    ch[x][y] = 1

    # 그렇지 않다면, 가능한 4개의 구간을 돈다
    for i in range(4):
        nx = x + dCol[i]
        ny = y + dRow[i]
        go(nx, ny, sum + arr[x][y], cnt + 1)

    # 방문 처리 풀어주기  ( 왜냐하면, 이후 다른 칸을 기준으로 진행될 때 여기도 방문시켜주어ㅑ 하기 때문이다 )
    ch[x][y] = 0


for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)

        if j + 2 < m:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if i - 1 >= 0:
                tmp2 = tmp + arr[i][j+1]
                ans = max(ans, tmp2)
            if i + 1 < n:
                tmp2 = tmp + arr[i+1][j+1]
                ans = max(ans, tmp2)
        if i + 2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if j + 1 < m:
                tmp2 = tmp + arr[i][j+1]
                ans = max(tmp2, ans)
            if j - 1 >= 0:
                tmp2 = tmp + arr[i][j-1]
                ans = max(tmp2, ans)

print(ans)
