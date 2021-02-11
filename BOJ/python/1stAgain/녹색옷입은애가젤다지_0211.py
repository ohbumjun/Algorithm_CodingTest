# 

# 첫번째 풀이 : 정통 ? 다익스트라 알고리즘 >> 시간초과
'''
2차원 배열 (i,j)를 하나의 노드로 보고
다익스트라 알고리즘을 수행하여
처음 idx에서 각 (i,j) idx까지의 거리 정보를
다익스트라 알고리즘으로 구한 다음

우리가 목표한 지점 idx의 거리정보를 출력했다

여기서 각 노드, (i,j)에 연결된 노드는
상,하,좌,우 ( 예외처리 포함 ) 에 연결된 노드이고
arr[i][j] 가 인접한 노드까지의 정보이다

최초 거리정보는 0이 아니라
arr[0][0] 이고,
여기서 출발한다 

'''
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

dC = [ -1 ,  0, 1, 0 ]
dR = [  0 , -1, 0, 1 ]

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    global N
    minVal = INF
    index = 0 # 가장 최단 거리가 짧은 노드의 index
    for i in range(N):
        for j in range(N):
            if distance[(i,j)] < minVal and not visited[(i,j)] :
                minVal = distance[(i,j)]
                index = (i,j)
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    global N
    # 시작 노드 초기화
    distance[(start[0],start[1])] = arr[start[0]][start[1]]
    visited[(start[0],start[1])]  = True
    # 거리 정보 재할당 
    for node in graph[(start[0],start[1])] :
        distance[node[0]] = node[1] + distance[(start[0],start[1])]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range( N * N -1) :
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost
order = 0
while True :
    order += 1
    N = int(input())
    if N == 0 :
        break
    
    INF      = int(1e9) # 무한을 의미하는 값
    arr      = [ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]
    visited  = {}
    distance = {}
    graph    = {}

    for i in range(N):
        for j in range(N):
            # 방문한 적이 있는지 체크하는 목적 리스트 만들기
            visited[(i,j)] = False
            # 최단 거리 테이블을 무한으로 초기화
            distance[(i,j)] = INF
            for k in range(4):
                cc = j + dC[k]
                rr = i + dR[k]
                if 0 <= cc < N and 0 <= rr < N :
                    if (i,j) not in graph.keys():
                        graph[(i,j)] = []
                    graph[(i,j)].append(( (rr,cc) , arr[rr][cc] ))
                
    dijkstra((0,0))

    print("Problem " + str(order) + ': ' + str(distance[(N-1,N-1)]))
