# https://www.acmicpc.net/problem/11724

# 1번째 풀이 : 그래프의 인접기반 리스트 구현 ---------------------------------------------------------------
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
sys.setrecursionlimit(10000)

def dfs(node) :
    visited[node] = True
    # 해당 요소의 인접기반 연결리스트 순회, 방문 안된 노드 방문 . 즉, 방문하게 되면, 현재 node랑 같은 연결요소에 속하게 된다. 
    for x in adj[node] :
        if not visited[x] :
            dfs( x ) 

nodes , paths = map(int,sys.stdin.readline().split())

# 인접기반 연결리스트 구현 > 연결리스트는 adj[정점] == 배열. 형태이다 .
adj = [ [ ] for _ in range(nodes + 1) ]  # [ [ ] * (nodes + 1) ] 가 아니다 !

visited = [ False ] * ( nodes + 1 )   # 방문한 정점은 다시 방문하지 않는다. 
cnt = 0

for _ in range(paths) :
    st, ed = map(int , sys.stdin.readline().split())
    adj[st].append(ed)
    adj[ed].append(st)

for i in range( 1, nodes + 1 ):
    if not visited[i]:
        # 우선 여기부터가 하나의 연결요소 시작
        cnt += 1
        dfs(i)


print( cnt ) 
