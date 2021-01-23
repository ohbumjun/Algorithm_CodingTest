# https://www.acmicpc.net/problem/1932
# Bottom_Up
import sys
from collections import deque


if __name__ == "__main__" :
    n = int(input())
    board = [ ]
    for i in range(n):
        board.append(list(map(int,input().split())))
    dy = [ [0] * n for _ in range(n) ]
    maxL = 0
    dy[0][0] = board[0][0]
    

    # 왼쪽 아래, 오른쪽 아래
    for i in range(1, n):
        dy[i][0] = dy[i-1][0] + board[i][0]
        dy[i][i] = dy[i-1][i-1] + board[i][i]

    # 그외
    for i in range(2,n):
        for j in range(len(board[i])):
            dy[i][j] = max( dy[i-1][j] , dy[i-1][j-1] ) + board[i][j]

    for i in range(n):
        maxL = max( maxL , dy[n-1][i] )

    print(maxL)
    



