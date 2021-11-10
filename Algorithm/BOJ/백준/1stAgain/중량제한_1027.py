# https://www.acmicpc.net/problem/1939

# 첫번째 풀이 : 메모리 초과 ( DFS )
from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

# 풀이 원리
# 1) 모든 경로의 가짓수를 구하고
# 2) 각 경로에서의 중량 최소값을 구하고 ( 각 경로의 중량 최소값을 구하는 이유 : 경로 중에서 가장
# 작은 중량이, 해당 경로로 갈 수 있는 최대중량값이 되기 때문이다
# ex) A->B : 3 중랴 , B->C : 2 중량이라면, A->C로 갈 수 있는 최대 중량은 2중량이다. )
# 3) 그 중에서의 최댓값을 구한다

# 같은 섬 사이에, 여러개 다리가 있을 수 있다
# --> 중복되는 경로 정보가 나온다면, 최대 경로 값으로 세팅하면 된다

# 즉, 쉽게 말해서, start에서 end 지점으로 갈 수 있는
# 모든 경로의 수를 조사해서 , 그 중에서 최대값을 구하는 원리를 적용했다
# 하지만, 메모리 초과 가 뜬다.
# 즉, 모든 경로를 조사하는 방법 보다 더 효율적으로 구현해야 함을 의미했다

# 그래프
graph = [[-1]*n for _ in range(n)]
for _ in range(m):
    st, ed, cst = map(int, input().split())
    st, ed = st-1, ed-1
    if graph[st][ed] != -1:
        graph[st][ed] = max(graph[st][ed], cst)
        graph[ed][st] = max(graph[ed][st], cst)
    else:
        graph[st][ed] = cst
        graph[ed][st] = cst


# 시작,끝점
st, ed = map(int, input().split())
# 체크 배열( 방문 여부 )
ch = [0] * n
cand = []
ans = 0


def go(end, cur, ch, val):
    global ans
    if cur == end:
        ans = max(ans, val)
        return
    for nxt in range(n):
        # cur 섬에서 다음 섬으로의 경로가 없다면 pass
        if graph[cur][nxt] == -1:
            continue
        # 해당 섬을 방문한 적이 있다면, pass
        if ch[nxt] == 1:
            continue
        ch[nxt] = 1
        go(end, nxt, ch, min(val, graph[cur][nxt]))
        ch[nxt] = 0


ch[st-1] = 1
go(ed-1, st-1, ch, int(1e9))
print(ans)

# -------------------------------------------------------------
# 2번째 풀이 : BFS + 이분 탐색 --> 메모리 초과
# 쉽게 말해서 mid 라는 중량제한값을 이분탐색을 통해 바꿔가면서
# 해당 mid 중량으로 st -> ed 까지 갈 수 있으면
# 더 큰값으로 mid를 찾아보고
# 갈 수 없으면 mid를 낮춰가면서
# 답을 찾아가는 과정
# 즉, mid 만큼의 중량을 가진 모의 트럭을 하나 두고
# 해당 경로로 가는 경우는 test 해가는 과정이라고 할 수 있다

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n, m = map(int, input().split())
maxW = 0


# 그래프
graph = [[-1]*n for _ in range(n)]
# 이부분에서 시간초과가 발생했다
# 이차원 배열을 아예 처음부터 박아두고 시작하는데
# 이렇게 하면, 사용되지 않는 , -1이 되는 부분도 생긴다
# 그런데 N이 무려 10000개 까지 있으므로
# 10000 * 10000 = 10^ 8
# 까다로운 경우, 메모리초과가 여기서 발생
for _ in range(m):
    st, ed, cst = map(int, input().split())
    st, ed = st-1, ed-1
    maxW = max(maxW, cst)
    if graph[st][ed] != -1:
        graph[st][ed] = max(graph[st][ed], cst)
        graph[ed][st] = max(graph[ed][st], cst)
    else:
        graph[st][ed] = cst
        graph[ed][st] = cst

# 시작,끝점
st, ed = map(int, input().split())
st, ed = st-1, ed-1

# bfs ( 해당 무게로 방문할 수 있는가 )


def bfs(weight):
    ch = [0]*n
    ch[st] = 1
    q = deque()
    q.append(st)
    while q:
        nxt = q.popleft()
        if nxt == ed:
            return True
        for i in range(n):
            # 1) 해당 섬으로의 경로가 존재
            # 2) 해당 섬 방문한 적 없음
            # 3) 해당 경로의 중량제한이, 현재 weight ( 모의 트럭 무게 ) 보다 크거나 같다면 ( 지나갈 수 있음 )
            if graph[nxt][i] != -1 and ch[i] == 0 and graph[nxt][i] >= weight:
                ch[i] = 1
                q.append(i)
    return False


# 이분 탐색
left = 0
right = maxW
ans = 0

while left <= right:
    mid = (left+right) // 2
    if bfs(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid

print(ans)

# -------------------------------------------------------------------
# 3번째 풀이 : 메모리 초과 해결
# 이차원 배열을 선언하되, 빈 배열에서 실제 경로만 append 하는 방향으로 메모리 세팅
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n, m = map(int, input().split())

# 그래프
graph = [[] for _ in range(n)]
for _ in range(m):
    st, ed, cst = map(int, input().split())
    st, ed = st-1, ed-1
    graph[st].append((ed, cst))
    graph[ed].append((st, cst))

# 시작,끝점
st, ed = map(int, input().split())
st, ed = st-1, ed-1

# bfs ( 해당 무게로 방문할 수 있는가 )


def bfs(weight):
    ch = [0]*n
    ch[st] = 1
    q = deque()
    q.append(st)
    while q:
        nxt = q.popleft()
        if nxt == ed:
            return True
        for nn, nc in graph[nxt]:
            # 1) 해당 섬으로의 경로가 존재
            # 2) 해당 섬 방문한 적 없음
            # 3) 해당 경로의 중량제한이, 현재 weight ( 모의 트럭 무게 ) 보다 크거나 같다면 ( 지나갈 수 있음 )
            if ch[nn] == 0 and nc >= weight:
                ch[nn] = 1
                q.append(nn)
    return False


# 이분 탐색
left = 0
right = 1000000000
ans = 0

while left <= right:
    mid = (left+right) // 2
    if bfs(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)
