# https://www.acmicpc.net/problem/1753

# 첫번째 풀이 : 시간초과 ( 정석 방법 ) -----------------------------
import heapq
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는, 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 노드방문여부 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리 짧은 노드 반환
# 즉, 그다음 방문할 노드를 선택해가는 과정
# 사실, 다른 말로하면, 이번에 방문한 노드와 인접한 노드중 가장 가까운 애


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijks(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드 제외한 전체 n-1 개의 노드에 대해 반복
    # n-1 번 노드를 선택하고, 그에 따른 거리 정보 update
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijks(start)

# 모든 노드로 가기 위한 최단 경로 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


# 두번째 풀이 : 시간초과 ( 정석 방법 ) -----------------------------
# 2가지 변화
# 1) 방문 처리를 위한 check 배열이 별도로 존재하지 않는다
# 2) 이제 우선순위 큐에다가 넣고, 그냥 우선순위큐가 빌때까지 반복한다.


# 처음 방문했을 때, 5로 저장 / 이후 또 그 노드를 방문해서 4으로 table 업데이트
# 그러면, 작업할 필요가 없겠지
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는, 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# def get_smallest_node(): >> 해당 기능은, heap 자료구조를 이용함으로써 해결된다


def dijks(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 ( 꺼내면 제일 거리 짧은 거 나올 것 )
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다
        # 예를 들어, 1번 노드를 방문했더니, 3번 노드가 인접하여 거리 5로 table update, 그 이후 queue에 넣음
        # 그런데, 다른 노드 방문하다가, 마찬가지로 3번 노드인접해서, 거리 3으로 table update , 그 이후 queue 에 넣음
        # 그러면, 현재 꺼내서 dist를 봤더니 5 , now는 3  // 이미 table, distance[now[는 3으로 되어있다면, 진행할 필요 없음
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijks(start)

# 모든 노드로 가기 위한 최단 경로 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
