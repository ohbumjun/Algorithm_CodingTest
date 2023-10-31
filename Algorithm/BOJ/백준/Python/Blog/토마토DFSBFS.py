# 1. 런타임 에러 코드
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
# 재귀 timeout set
sys.setrecursionlimit(10**6) # 이것을 넘어가면 python 재귀 종료시키기

dx = [-1,0,1,0]
dy = [ 0,1,0,-1]

# board
col,row = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(row)]
dis = [ [0] * col for _ in range(row) ]
Q = deque()
res = -12999999

# 모든 익은 토마토 들에 대해서 각각 BFS를 적용해야 한다
# ex. dis 배열 을 각 BFS마다 초기화 해주고
# 한칸씩 더 나아갈 때마다, cnt += 1 을 해준다
# 각 BFS가 끝날 때마다 cnt를 res에 넣어준다

# 1) 전체를 돌면서, 익은 토마토의 idx 정보를 넣어준다
for i in range(row):
    for j in range(col):
        if board[i][j] == 1 :
            Q.append((i,j))

while Q :
    now = Q.popleft()
    for i in range(4):
        xx = now[0] + dx[i]
        yy = now[1] + dy[i]
        if 0 <= xx < row and 0 <= yy < col  and board[xx][yy] == 0 :
            # 1로 바꿔서 방문 처리
            board[xx][yy] = 1
            # dis 배열 update
            dis[xx][yy] = dis[now[0]][now[1]] + 1
            # Q에 넣어주기
            Q.append((xx,yy))

# 모두 익는지 , 익지 못하는지 확인
flag = 1
for i in range(row):
    for j in range(col):
        # 여전히 안 익은 토마토가 존재하더
        if board[i][j] == 0 :
            flag = 0

# 최소값 찾기
if flag == 1:
    # 모두 익었다는 것
    for i in range(row):
        for j in range(col):
            if dis[i][j] > res : 
                res = dis[i][j]
    print(res)
else:
    print(-1)


# 런타임 해결 코드
# 1) newX, newY를 설정할 때, 매번 반복문마다 새로 값 할당하는 것이 아니라, 미리 할당해두고 for문 돌리기
# 2) dis배열에 값을 저장하고, 이후에 brute-force-algorithm을 통해, 
# 모든 dis배열을 돌면서, 최대값을 구하는 것이 아니라
# bfs 내에서, 각 bfs 레벨을 확장할때마다 count를 더하여 값을 미리 구하는 방식을 취한다
# 3) 토마토가 익었는지, 익지 않았는지를 볼때도, flag = 0을 해두고 모든 배열 도는 것이 아니라, 중간에 return -1 
