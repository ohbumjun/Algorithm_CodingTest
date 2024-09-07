# BFS : 시간 초과
# https://www.acmicpc.net/problem/7569

import sys
sys.stdin = open("input.txt", "rt")
import heapq as hq
from collections import deque

col, row, Z = map(int,input().split()) 
board = []

for _ in range(Z):
    oneStep = [ list(map(int, input().split() )) for _ in range(row) ]
    board.append(oneStep)

dis   = [ [ [0] * col for _ in range(row) ]  for _ in range(Z) ]
queue = deque([])


dCol = [ -1, 0, 1,  0 , 0,  0] # 좌, 하, 우, 상  
dRow = [ 0,  1, 0, -1 , 0 , 0]
dZ   = [ 0 , 0, 0,  0 , 1, -1]


# 익은 애들 찾고
for z in range(Z):
    for i in range(row) :
        for j in range(col) :
            if board[z][i][j] == 1 :
                queue.append((z,i,j))  # j는 row 정보 , i는 col 정보

# queue 가 빌때까지 된다
while queue :
    now = queue.popleft()
    nowZ = now[0] # z 축
    nowX = now[1] # row 
    nowY = now[2] # col

    for i in range(6):
        zz = nowZ + dZ[i]
        xx = nowX + dRow[i]
        yy = nowY + dCol[i]
        if 0 <= zz < Z and 0 <= xx < row and 0 <= yy < col and board[zz][xx][yy] == 0 :
            # 방문 처리
            board[zz][xx][yy] = 1
            # queue에 넣고
            queue.append((zz,xx,yy))
            # 거리 계산해주기
            dis[zz][xx][yy] = dis[nowZ][nowX][nowY] + 1

# 순회하면서 최소 dis 값 찾기
maxD = 0
for z in range(Z):
    for i in range(row) :
        for j in range(col) :
            if board[z][i][j] == 0 :
                print(-1)
                break
            elif dis[z][i][j] > maxD :
                maxD = dis[z][i][j]
else:
    print(maxD)
                

    

# 토마토 성공본  --------------------------------------------------------------
'''
여기서 주의할 점은, 
1) 위와 같이 각 토마토까지의 거리 정보를 저장하는 dis 배열을 따로 만드는 것이 아니라
day라는 변수를 하나 선언해서 queue의 한 cycle이 돌아갈 때마다 1을 더해주는 것이다
queue에는 같은 날 익은 토마토의 목록이 들어있고
queue를 모두 돌아서 , 그 옆의 토마토들을 queue에 다시 넣는 작업은 곧 1일이 지났다는 것이다

2) 이중 for문을 통해 queue 단위, day 단위의 for문을 만드는 것이 포인트
즉, 위의 코드와 달리 queue, day 단위를 표시해주기 위해 이중 for문 형태의 코드를 짰으며
여기의 경우, pop을 사용하면 안되기 때문에
tmp라는 임시 덱을 선언, 근접한 토마토 목록들을 tmp에 추가해주고
그것을 다시 queue에 update 시켜주는 방식을 활용한다 . 

3) day가 0 이 아니라 -1로 초기화 해주는 이유는, 
queue에서 빠지는 순간, 빠진 토마토들이 +1 day로 쳐지는 것
즉, 맨처음에는 1이 들어가 있고
그 이후 , 옆에 근접한 0 토마토들이 queue에 들어가게 된다.

그리고 queue에 처음 익혀야 하는 토마토들이 들어가는 순간 부터가 day 0 인 것이다 ( 뭔말인지 아직 잘 모름 ;;)
'''
from collections import deque

col, row, Z = map(int,input().split())
board = [[list(map(int, input().split())) for _ in range(row)] for _ in range(Z)]
queue = deque([])
days   = -1


dCol = [ -1, 0, 1,  0 , 0,  0] # 좌, 하, 우, 상  
dRow = [ 0,  1, 0, -1 , 0 , 0]
dZ   = [ 0 , 0, 0,  0 , 1, -1]


# 익은 애들 찾고
for z in range(Z):
    for i in range(row) :
        for j in range(col) :
            if board[z][i][j] == 1 :
                queue.append((z,i,j))  # j는 row 정보 , i는 col 정보

# queue 가 빌때까지 된다
tmp = deque([])
while queue :
    for  pos in queue : 
        nowZ = pos[0] # z 축
        nowX = pos[1] # row 
        nowY = pos[2] # col

        for i in range(6):
            zz = nowZ + dZ[i]
            xx = nowX + dRow[i]
            yy = nowY + dCol[i]
            if 0 <= zz < Z and 0 <= xx < row and 0 <= yy < col and board[zz][xx][yy] == 0 :
                # 방문 처리
                board[zz][xx][yy] = 1
                # tmp !! queue가 아니라 , 에 넣고
                tmp.append((zz,xx,yy))
    # 한번 큐 단계를 통해 거리도 1 증가
    days += 1
    queue = tmp
    tmp = []

# 순회하면서 최소 dis 값 찾기

res = 0

for z in range(Z):
    for i in range(row) :
        for j in range(col) :
            if board[z][i][j] == 0 :
                print(-1)
                exit(0)
else:
    print(days)
                
