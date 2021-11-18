# https://www.acmicpc.net/submit/16398/35563479

# 크루스칼 --- 
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

# 프림 --- 
N    = int(input())
csts = [list(map(int,input().split())) for _ in range(N)]


def prim(W):
    dists   = [int(1e9)] * N
    nearest = [int(1e9)] * N
    edges   = []
    # 시작 노드 : 0
    dists[0],nearest[0] = -1,-1
    for i in range(1,N):
        dists[i],nearest[i] = W[0][i],0
    # N-1 개의 노드 추가적 선택
    for _ in range(N-1):
        mDist,mIdx = int(1e9),-1
        for i in range(N):
            if dists[i] > 0 and dists[i] < mDist :
                mDist,mIdx = dists[i],i
        edges.append((mDist,mIdx,nearest[mIdx]))
        dists[mIdx] = -1
        for i in range(N):
            if dists[i] > 0 and dists[i] > W[mIdx][i] :
                dists[i] = W[mIdx][i]
                nearest[i] = mIdx
    return edges

edges = prim(csts)
print(sum(edge[0] for edge in edges))
        
        
