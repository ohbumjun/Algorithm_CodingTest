# https://programmers.co.kr/learn/courses/30/lessons/42861

# 크루스칼
from collections import defaultdict
import heapq as hq


def find_parent(parent, v):
    print("v")
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]


def union_parent(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, costs):
    '''
    크루스칼 알고리즘 
    모든 정점을 방문하는 , 사이클을 형성하지 않으면서
    최소 거리를 구하는 문제라고도 할 수 있다 
    '''
    answer = 0
    parent = [0] * n
    sort_cost = []
    for cost in costs:
        st, ed, cst = cost
        sort_cost.append((cst, st, ed))
    costs = sorted(sort_cost)
    for i in range(n):
        parent[i] = i
    for cost in costs:
        cst, st, ed = cost
        if find_parent(parent, st) != find_parent(parent, ed):
            union_parent(parent, st, ed)
            answer += cst
    return answer

# 프림


def prim(W):
    n = len(W) - 1  # 5개 정점 지남
    F = []
    distance = [-1] * (n+1)
    nearest = [-1] * (n+1)

    # 1번 정점
    for i in range(2, n+1):
        distance[i] = W[i][1]
        nearest[i] = 1

    # n-1개의 정점을 추가로 선택
    for i in range(n-1):
        # 최소 거리를 찾는다
        minV = int(1e9)
        for j in range(2, n+1):
            if distance[j] > 0 and distance[j] < minV:
                minV = distance[j]
                vnear = j
        edge = (W[vnear][nearest[vnear]])
        F.append(edge)
        print()
        distance[vnear] = -1
        # 위치, 거리 정보 update
        for j in range(2, n+1):
            if distance[j] > W[j][vnear]:
                distance[j] = W[j][vnear]
                nearest[j] = vnear
    return F


def solution(n, costs):
    '''
    프림 알고리즘 
    모든 정점을 방문하는 , 사이클을 형성하지 않으면서
    최소 거리를 구하는 문제라고도 할 수 있다 
    '''
    # 최대값 초기화
    W = [[int(1e9)]*(n+1) for _ in range(n+1)]
    for cost in costs:
        st, ed, cst = cost
        st += 1
        ed += 1
        W[st][ed] = cst
        W[ed][st] = cst
    for w in W:
        print(w)
    edges = prim(W)
    return sum(edges)

# prim 알고리즘 : 간선 기준 Lazy Solution


def prim(n, costs):
    mst = []
    # 간선 정보 저장
    adj_edges = defaultdict(list)
    # 방문할 간선 정보 저장 공간
    for cost in costs:
        n1, n2, w = cost
        # heap을 적용하기 위해서 weight, 간선 비용을 맨 처음 원소로 집어넣는다
        adj_edges[n1].append((w, n1, n2))
        adj_edges[n2].append((w, n2, n1))
    # 방문한 간선 정보 저장 공간
    explored = set()
    explored.add(0)
    # 그 다음 방문할 간선
    toVisit = adj_edges[0]
    hq.heapify(toVisit)

    # mst
    mst.append(0)
    while toVisit:
        weight, stN, edN = hq.heappop(toVisit)
        if edN not in explored:
            explored.add(edN)
            mst.append(weight)
            for w, s, e in adj_edges[edN]:
                if e not in explored:
                    hq.heappush(toVisit, (w, s, e))
    return sum(mst)


def solution(n, costs):
    return prim(n, costs)
