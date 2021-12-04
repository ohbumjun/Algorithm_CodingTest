# https://www.acmicpc.net/problem/1956


INT_MAX = int(1e9) 
V,E     = map(int,input().split())
graph   = [[INT_MAX] * V for _ in range(V)] 
edges   = []
ans     = -1

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

def find_length(target, length):
    global parent
    # print("target, parent[target], length", target, parent[target], length)
    if parent[target] == target :
        return length
    return find_length(parent[target], length + graph[parent[target]][target])

# 부모 초기화 
parent = [i for i in range(V)]

for _ in range(E):
    st,ed,cst = map(int,input().split())
    st,ed     = st - 1, ed - 1
    edges.append((cst,st,ed))
    graph[st][ed] = cst

# 플로이드 와샬을 통해서 각 정점에서 다른 정점 까지의 최소 거리 구하기
dp = [[INT_MAX] * V for _ in range(V)]
# 자기 자신까지의 거리 0
for i in range(V):
    dp[i][i] = 0
# 거리 정보 복사 
for r in range(V):
    for c in range(V):
        dp[r][c] = graph[r][c]
# 거리 구하기
for k in range(V):
    for r in range(V):
        for c in range(V):
            if k == r or k == c : continue
            dp[r][c] = min(dp[r][c], dp[r][k] + dp[k][c])

# 경로 x = -1 
for r in range(V):
    for c in range(V):
        if dp[r][c] == INT_MAX :
            dp[r][c] = -1
            

# 간선들 정렬
edges.sort()

# print(edges)

for i in range(E):
    cst,st,ed = edges[i]
    if find_parent(parent, st) != find_parent(parent, ed) :
        union_parent(parent, st, ed)
# print("final parent", parent)
        
for i in range(E):
    cst,st,ed = edges[i]
    # 서로 가는 길이 있다면 : 서로로 가는 경로의 합이 싸이클 경로 
    if dp[st][ed] != -1 and dp[ed][st] != -1 :
        s  = dp[st][ed] + dp[ed][st]
        if ans == -1 or ans > s :
            ans = s
    # 부모가 같다면
    if find_parent(parent, st) == find_parent(parent, ed):
        if dp[ed][parent[ed]] != -1 : # 도착점에서, 부모로 가는 길이 있다면 
            s = dp[parent[ed]][ed] + dp[ed][parent[ed]] # 부모 -> 도착 + 도착 -> 부모 
            if ans == -1 or ans > s :
                ans = s

print(ans if ans != -1 else -1)
        