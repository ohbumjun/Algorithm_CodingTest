# https://www.acmicpc.net/problem/1922


# kruskal 알고리즘
import sys
from collections import deque, Counter
sys.setrecursionlimit(100000)


class DisjointSet:
    def __init__(self, n):  # n : n개의 노드
        self.U = []  # 부모 집합
        for i in range(n):
            # 자기 자신을 부모로 갖게 한다
            self.U.append(i)

    # 부모 찾는 함수
    def find(self, i):
        j = i
        while(self.U[j] != j):
            # 자가자신의 부모가, 자기 자신을 가리킬 때까지
            # 밑에서부터 위로 올라간다
            j = self.U[j]
        return j

    '''
    여기서 self란, 
    자신을 호출한 instance, object를 의미하게 되는 것이다
    예를 들어,

    D1 = DisjointSet(n)
    D2 = DisjointSet(n)
    이라고 하면

    D1.union()을 하게 될시
    DisjointSet class 내의 union 함수가 실행될 것인데,
    여기서 union함수는 궁금해 할 것이다
    오케이..내가 호출되서, union 함수를 실행할 것이긴 한데...
    누군에 대한 update ?
    D1 ?
    D2 ?

    이때 바로 self가 역할 하는 것이다
    self에는 자신을 호출한 D1 에 대한 정보가 들어감으로써
    update() 로 하여금 
    아 ~~~ D1 update ? okay !

    self는 마치 포인터 같은 것이다
    instance를 만들 때마다, 메모리에 새로운 공간이 만들어지고
    그 새로운 공간에 instance 정보가 할당된다

    self는 포인터 역할을 하여,
    특정 instance가 위치한 메모리 정보를 가리켜 주는 것이다 
    '''

    def union(self, p, q):
        if(p < q):
            self.U[q] = p
        else:
            self.U[p] = q

    # find 함수를 통해 p, q 에 대한 루트 노드를 반환 받으면
    # 비교하여 setting 한다
    def equal(self, p, q):
        if(p == q):
            return True
        else:
            return False

# 크루스칼 알고리즘


def kruskal(n, E):  # E : 가중치 순서대로 sort된 상태여야 한다
    F = []
    dset = DisjointSet(n)  # n만큼 disjoint set을 만든다, n은 정점 집합의 크기
    while(len(F) < n - 1):  # F의 size가 n-1이 될때까지 ( edge의 개수 )
        edge = E.pop(0)  # 앞의 것을 뽑는다.
        i, j = edge[0], edge[1]
        p = dset.find(i-1)  # 루트 노드를 찾는다
        q = dset.find(j-1)

        # 사이클을 형성하지 않는다면
        if(not dset.equal(p, q)):  # 집합이 서로 다르다면
            dset.union(p, q)  # 집합을 합친다
            F.append(edge)
            # print("accepted", edge)
        # 버려진 것을 확인하기
        # else:
            # print("discarded", edge )
    return F


node = int(sys.stdin.readline())
path = int(sys.stdin.readline())
E = []
res = 0

for _ in range(path):
    st, ed, cost = map(int, sys.stdin.readline().strip().split())
    E.append([st, ed, cost])

# E를 가중치 순으로 sort
E.sort(key=lambda x: x[2])

F = kruskal(node, E)


for f in F:
    res += f[2]

print(res)

# 크루스칼  ----
def find_parent(arr, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(arr, a, b):
    # 맨처음에는 자기 자신의 값으로 parent가 설정되어 있다 ex) 1, 4
    # 이 경우에는, 그냥 큰 애에다가, 작은 애를 합친다
    a = find_parent(arr, a)
    b = find_parent(arr, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
edges = []
parent = [-1] * (n+1)
res = 0

# 부모 정보 초기화
for i in range(len(parent)):
    parent[i] = i

for _ in range(m):
    st, ed, cost = map(int, input().split())
    edges.append((cost, st, ed))
# edges 정렬
edges.sort()
for edge in edges:
    cost, st, ed = edge
    if find_parent(parent, st) != find_parent(parent, ed):
        res += cost
        union(parent, st, ed)
print(res)

# prim 알고리즘
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


def prim(W):  # W : 입력받은 연결 정보
    # 초기화 작업
    # len(W) 이란, 노드의 개수를 말하는 것이다. 그런데, 우리는 W에 임의의 노드 개수 1을 추가했다
    # n 은 사실상, 실제 노드의 개수를 말하게 될 것이다.
    n = len(W) - 1
    F = []
    nearest = [-1] * (n + 1)
    distance = [-1] * (n + 1)

    # 1 노드를 시작점으로 setting 하여 초기화
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]

    for _ in range(n-1):  # n - 1개의 edge가 선택될 때까지 반복
        minVal = 10001
        for i in range(2, n + 1):
            '''
            Y에 선택되지 않은 노드 중에서
            Y집단에 가장 가까운 거리에 있는 노드를 선택하는 과정 
            '''
            if(0 <= distance[i] and distance[i] < minVal):
                minVal = distance[i]
                vnear = i  # vnear에는 Y에 속하지 않은 노드 중, Y에 가장 가까운 노드가 들어간다

        edge = (nearest[vnear], vnear, W[nearest[vnear]][vnear])
        F.append(edge)  # 프림 알고리즘 진행 과정에서 선택한 edge 정보가 들어간다
        distance[vnear] = -1

        # 자. 이제 다시 distance[i] 값들을 update 시켜주어야 한다
        # Y에 vnear라는 새로운 노드가 추가되었기 때문에
        # vnear라는 노드와의 거리를 기준으로 다시 distance[i]를 update 시켜주어야 한다는 것이다
        for i in range(2, n+1):
            if(distance[i] > W[i][vnear]):
                distance[i] = W[i][vnear]
                nearest[i] = vnear  # 가장 가까운 node 정보고 update
    return F
#


# 최대비용 : 10001
nodes = int(sys.stdin.readline())
paths = int(sys.stdin.readline())
W = [[10001] * (nodes + 1) for _ in range(nodes + 1)]
res = 0

# 0번째 col, 0번째 row는 -1로 초기화해준다
for i in range(nodes + 1):
    W[0][i] = -1

for i in range(nodes + 1):
    W[i][0] = -1

# 자기 자신까지의 거리는 0으로 만들어준다
for i in range(1, nodes + 1):
    W[i][i] = 0

# 연결정보를 저장한다.
for _ in range(paths):
    st, ed, cost = map(int, sys.stdin.readline().strip().split())
    W[st][ed] = cost
    W[ed][st] = cost

F = prim(W)

for f in F:
    res += f[2]

print(res)
