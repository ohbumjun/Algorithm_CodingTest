# https://www.acmicpc.net/problem/16947

'''
< Notion 참고 > 

문제의 조건상

순환선 == 싸이클. 이라고 해석할 수 있다 
< 정의 : '싸이클' >
'경로'인데,
'시작점, 도착점'이 같은 싸이클을 의미한다 

N개의 정점과, N - 1개의 간선으로 이루어져 있는 그래프는 '트리'이다 
'트리'의 특징 중 하나는 
'싸이클'이 없다 .라는 것이다 

그리고 이러한 '트리'에 '간선'을 1개 추가하면 
'싸이클'이 생기고
이때 '싸이클'은
1가지만 생기게 되는 것이다 

< 문제 >
모든 정점과, 순환선이
얼마나 서로 떨어져 있는가 

< 해결 과정 >
1) 순환선 ( 싸이클 ) 찾기
2) 정점과 순환선 사이의 거리 : DFS, BFS 이용하기  >> 순환선의 정점을, 모두 시작점으로 해주고, DFS, BFS 알고리즘을 이용하여, 거리를 계산하는 것이다 


그렇다면, '순환선' 및 '싸이클'은 어떻게 찾을 수 있을까 ??
특정 시작점을 잡고
방문할 때마다 스택에 쌓아가고
방문처리를 해준다 

그 이후 방문할 곳이 없다면, 다시 되돌아 오는데
이때 스택에서 빼준다.
이러한 과정을 반복하다

결국, 더이상 아무데도 갈곳이 없을 때,
즉, 다른 정점으로 갈 수도 없고
되돌아갈 수도 없을 때

그때 '스택'에 남아있는 값이 바로
'싸이클 및 순환선'이 되는 것이다 

'''


import sys
import heapq
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
1) 먼저 싸이클을 생성해야 한다

check
0 : 아직 방문 안함
1 : 방문함
2 : 방문했는데 싸이클

return
x : 해당 정점이 시작점 ( 싸이클 형성 )
-1 : 싸이클 못찾음
-2 : 싸이클 찾음, 그러나 얘는 싸이클 포함 x 

'''
n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for _ in range(n):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)


def go(x, p):  # p : 이전에 방문한 정점
    if check[x] == 1:
        return x
    check[x] = 1
    for node in graph[x]:
        if node == p:
            continue
        res = go(node, x)
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res:  # 이후 부터는 -2리턴
                return -2
            else:
                return res
    return -1


go(1, -1)

'''
각 정점에서
싸이클 까지의 거리 판단 : BFS

< 처음 생각한 방법 >
1)for문으로 모든 정점 돈다
2) check[x] == 2 라면 0
3) 아니라면,queue에 넣고 진행
dist = 1 로 세팅 
3) queue 에 있는 것을 뺀다
- 해당 정점과 연결된 정점들을 조사하면서
- check[adjNode]를 확인한다
- 2 인 정점이 있다면 dist를 출력한다
4) 다 돌고나서도 없으면 dist += 1

< 위의 과정을 진행하면 모든 정점에 대해 while문을 해주는 것 : 비효율 ?
< 개선 방법 >
- 사이클 내에 존재하는 모든 정점을 queue에 포함시킨다
- queue 내의 정점들을 돌면서, 싸이클에 포함되지 않은 정점들의
dist 정보를 현재 queue에서 꺼낸 정점의 dist + 1을 해준다
- 한번의 while문으로, 모든 정점의 , 싸이클까지의 거리 파악 가능 

'''

queue = deque()  # 싸이클에 포함된 애들 목록
dist = [-1] * (n + 1)

for i in range(1, len(check)):
    if check[i] == 2:
        dist[i] = 0
        queue.append(i)
    else:
        dist[i] = -1


while queue:
    q = queue.popleft()
    for y in graph[q]:
        if dist[y] == -1:
            queue.append(y)
            dist[y] = dist[q] + 1

for i in range(1, len(dist)):
    print(dist[i], end=' ')
