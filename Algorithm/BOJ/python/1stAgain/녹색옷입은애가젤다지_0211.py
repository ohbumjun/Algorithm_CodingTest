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
from collections import deque
import math
import heapq
from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dC = [-1,  0, 1, 0]
dR = [0, -1, 0, 1]

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    global N
    minVal = INF
    index = 0  # 가장 최단 거리가 짧은 노드의 index
    for i in range(N):
        for j in range(N):
            if distance[(i, j)] < minVal and not visited[(i, j)]:
                minVal = distance[(i, j)]
                index = (i, j)
    return index

# 다익스트라 알고리즘


def dijkstra(start):
    global N
    # 시작 노드 초기화
    distance[(start[0], start[1])] = arr[start[0]][start[1]]
    visited[(start[0], start[1])] = True
    # 거리 정보 재할당
    for node in graph[(start[0], start[1])]:
        distance[node[0]] = node[1] + distance[(start[0], start[1])]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(N * N - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


order = 0
while True:
    order += 1
    N = int(input())
    if N == 0:
        break

    INF = int(1e9)  # 무한을 의미하는 값
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = {}
    distance = {}
    graph = {}

    for i in range(N):
        for j in range(N):
            # 방문한 적이 있는지 체크하는 목적 리스트 만들기
            visited[(i, j)] = False
            # 최단 거리 테이블을 무한으로 초기화
            distance[(i, j)] = INF
            for k in range(4):
                cc = j + dC[k]
                rr = i + dR[k]
                if 0 <= cc < N and 0 <= rr < N:
                    if (i, j) not in graph.keys():
                        graph[(i, j)] = []
                    graph[(i, j)].append(((rr, cc), arr[rr][cc]))

    dijkstra((0, 0))

    print("Problem " + str(order) + ': ' + str(distance[(N-1, N-1)]))

# 두번째 풀이 :  heap 이용
sys.setrecursionlimit(1001*1001)

'''
잃을 수 밖에 없는 최소 금액
최대한, 도둑 루피가 최소인 칸들만 지나서
해당 정점으로 가야 한다는 것

만약 잃을 수 밖에 없는 최소 금액 == 거리.
라고 한다면

이는 곧, 최소인 거리를 지나서, 해당 정점까지 가는
경우의 수를 구하는
문제와 같다 .

다익스트라를 통해 실행하고

플로이드 와샬을 통해 실행한다 

'''
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
i = 1
INF = int(1e9)
while True:
    n = int(input())
    if n == 0:
        break
    # 그래프 세팅 : hash table이용
    dist = dict()
    rupy = dict()
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 간선 연결 정보 setting
    for x in range(n):
        for y in range(n):
            rupy[(x, y)] = []
            # { (x,y) : [] , ......  } --> [] :( 연결된 정점좌표 , 해당 좌표까지 거리  )
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or n <= nx or ny < 0 or n <= ny:
                    continue
                rupy[(x, y)].append(((nx, ny), arr[nx][ny]))
            # dist 세팅
            dist[(x, y)] = INF

    # 다익스트라 시작
    # 초기화
    q = []
    dist[(0, 0)] = arr[0][0]
    heapq.heappush(q, ((0, 0), dist[(0, 0)]))

    while q:
        pos, dis = heapq.heappop(q)
        x, y = pos[0], pos[1]
        if dis > dist[(x, y)]:
            continue
        for nxt in rupy[(x, y)]:
            cost = dis + nxt[1]
            if dist[nxt[0]] > cost:
                dist[nxt[0]] = cost
                heapq.heappush(q, (nxt[0], cost))
    print("Problem %d: %d" % (i, dist[(n-1, n-1)]))
    i += 1
