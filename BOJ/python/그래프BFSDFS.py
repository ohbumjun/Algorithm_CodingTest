# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, m, st = map(int,input().split())
board = [ [0] * ( n + 1) for _ in range( n + 1 ) ]

for _ in range(m):
    line = list(map(int, input().split()))
    board[line[0]][line[1]] = 1
    board[line[1]][line[0]] = 1

# BFS
def bfs(start):
    visited = [start]
    Q = deque([start])
    while Q :
        now = Q.popleft()
        for node in range(len(board[now])):
            if board[now][node] == 1 and node not in visited :
                visited.append(node)
                Q.append(node)
    return visited 
        
# DFS
def dfs(start,visited):
    visited.append(start)
    for node in range(len(board[start])):
        if board[start][node] == 1 and node not in visited :
            dfs(node,visited)
    return visited

# * in python : 컨테이터 타입의 데이터를 unpacking
# 아래 * 를 붙임으로써, 데이터 내용들만을 추출할 수 있다
print(*dfs(st,[]))
print(*bfs(st))
    

    
    
        
        
