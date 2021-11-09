# https://programmers.co.kr/learn/courses/30/lessons/49189

import heapq
INF = int(1e9)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for eg in edge:
        a, b = eg
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    q = []
    distance[1] = 0
    heapq.heappush(q, (1, 0))
    while q:
        n, d = heapq.heappop(q)
        if d > distance[n]:
            continue
        for nd, dis in graph[n]:
            dis += d
            if dis < distance[nd]:
                distance[nd] = dis
                heapq.heappush(q, (nd, dis))
    maxD = 0
    for i in range(1, n+1):
        if maxD < distance[i]:
            maxD = distance[i]
    for i in range(1, n+1):
        if distance[i] == maxD:
            answer += 1
    return answer
