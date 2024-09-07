# https://www.acmicpc.net/problem/1260

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

def bfs(num):
    queue = deque([])
    queue.append(num)
    ch[num] = 1

    while queue:
        nowNode = queue.popleft()
        print(nowNode, end = ' ')
        # sorted가 필요한 이유는, 이 문제에서, 낮은 우선순위부터 출력하라고 했기 때문이다. 
        for n in sorted(adj[nowNode]):
            if ch[n] == 0 :
                ch[n] = 1
                queue.append(n)

def dfs(start) :
    ch[start] = 1
    print(start, end = ' ')
    for n in sorted(adj[start]):
        if ch[n] == 0 :
            dfs(n)
    

nodes, edges, st = map(int, sys.stdin.readline().split())
adj =[ [] for _ in range(nodes + 1) ]
ch = [0] * ( nodes + 1 ) 

for _ in range(edges):
    n1, n2 = map(int, sys.stdin.readline().split())

    adj[n1].append(n2)
    adj[n2].append(n1)

# DFS
dfs(st)
print()
# 정점 초기화
for i in range(len(ch)):
    ch[i] = 0
# BFS
bfs(st)


    
    
        
        
