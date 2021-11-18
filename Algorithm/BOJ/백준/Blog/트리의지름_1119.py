# https://www.acmicpc.net/submit/16398/35563479

N    = int(input())

csts = [list(map(int,input().split())) for _ in range(N)]

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

# 부모 세팅 
parent = [-1] * N
for i in range(N): parent[i] = i

# edge 목록 파악하기
edges = []
for r in range(N) :
    for c in range(r):
        if csts[r][c] == 0 : continue
        edges.append((csts[r][c],r,c))
edges.sort()

ans = 0
for cst,st,ed in edges :
    if find_parent(parent,st) != find_parent(parent,ed) :
        union_parent(parent,st,ed)
        ans += cst
print(ans)