# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
# 재귀 timeout set
sys.setrecursionlimit(10**6) # 이것을 넘어가면 python 재귀 종료시키기

# 상하 좌우
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n , m = map(int, input().split())
board = [ list(input()) for _ in range(n) ]
dis   = [ [0] * m for _ in range(n) ]

Q = deque()

# 현재 위치를 Q에 넣는다.
Q.append((0,0))

# 이미 방문한 곳 벽으로 만들어버릭
board[0][0] = 0 

while Q :
    
    now = Q.popleft()
    nowX = now[0]
    nowY = now[1]

    if nowX == n-1 and nowY == m - 1 :
        print(dis[nowX][nowY] + 1)
        break


    for i in range(4):
        
        newX = nowX + dx[i]
        newY = nowY + dy[i]
        if 0 <= newX < n and 0 <= newY < m and board[newX][newY] == '1' :
            # 00으로 바꿔준다.
            board[newX][newY] = 0

            # dis 배열
            dis[newX][newY] = dis[nowX][nowY] + 1 

            # Q에 넣는다.
            Q.append((newX,newY))


        

