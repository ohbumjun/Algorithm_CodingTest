# https://www.acmicpc.net/problem/2468

# BFS
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(10000)

n = int(input())
dCol = [-1,0,0,1]
dRow = [0,-1,1,0]
cnt = 0
res = 0
arr = [ list(map(int,input().split())) for _ in range(n) ]


for h in range(0 , 100) :
    
    ch = [ [0] * n for _ in range(n) ]
    
    queue = deque([])
    # 첫 row부터 접근한다
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and ch[i][j] == 0:
                ch[i][j] = 1
                queue.append((i,j))
                while queue :
                    q = queue.popleft()
                    nowRow = q[0]
                    nowCol = q[1]
                    for k in range(4):
                        rr = nowRow + dRow[k]
                        cc = nowCol + dCol[k]
                        if 0 <= rr < n and 0 <= cc < n and arr[rr][cc] > h and ch[rr][cc] == 0 :
                            ch[rr][cc] = 1
                            queue.append((rr,cc))
                cnt += 1
    res = max(res,cnt)
    if cnt == 0 :
        break

print(res)




## DFS
n = int(input())
dCol = [-1,0,0,1]
dRow = [0,-1,1,0]
res = 0
arr = [ list(map(int,input().split())) for _ in range(n) ]

def DFS(x,y,h):
    # 방문표시
    ch[x][y] = 1

    for i in range(4):
        xx = x + dRow[i]
        yy = y + dCol[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and arr[xx][yy] > h :
            DFS(xx,yy,h)

# max 값 찾기, minH 찾기
maxH = 0
minH = 14123213
for i in range(n):
    for j in range(n):
        if arr[i][j] > maxH :
            maxH = arr[i][j]
        if arr[i][j] < minH :
            minH = arr[i][j]

for h in range( minH, maxH ) :
    
    ch = [ [0] * n for _ in range(n) ]
    queue = deque([])
    # 첫 row부터 접근한다
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and ch[i][j] == 0 :
                cnt += 1
                DFS(i,j,h)

    res = max(res,cnt)
    if cnt == 0:
        break
print(res)

'''
arr 라는 배열은 건드리면 안된다 .
arrCopy = arr 라는 식으로 식을 진행하더라도 ,
arrCopy 의 변경사항이 arr 에 반영되어버린다.
'''