# 트리의 지름
# https://www.acmicpc.net/problem/1967

'''
알고리즘의 이해  /

서로 가장 멀리 있는 노드를 찾아야 한다.
분명한 것은, 두 노드는 모두 말단 노드일 것이다.

1. 루트1번을 시작으로 해서, 가장 긴( 먼거리 ) 에 있는 즉,
가중치가 끝 노드를 DFF 탐색으로 찾는다.

가장 긴 지름 ??

적어도 하나는 무조건, 루트 노드 기준
가장 멀리 있을 거니까

2. 찾은 끝 노드를, 다시 루트 노드로 설정하여
DFS 탐색을 통해, 길이를 더해나간다.
즉, 루트노드에서 가장 멀리 떨어져있는 노드를 중심으로,
또 가장 멀리 있는노드를 찾는다. 

3. 탐색하며 더한 가중치 값들 중 
최댓값을 출력하면, 트리의 지름이 된다. 


여기서 탐색은 DFS로 진행했으며 ,
탐색을 진행하면서, 가중치 값들을 계속 더해간다.

'''
# DFS ------------------------------
import heapq as hq
from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


def dfs(start, tree, weight):
    # start : 스타트 노드
    # tree : 우리가 순회하는 트리
    # weight : 우리가 저장할 weight 배열
    # ch : 이미 방문한 노드는 다시 방문하지 않기 위해 ch 설정
    ch[start] = 1

    for node, w in tree[start]:
        if ch[node] == 0:
            ch[node] = 1
            weight[node] = weight[start] + w
            print("start, node, weight", start, node, weight[node])
            dfs(node, tree, weight)


n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
ch = [0] * (n + 1)

# 입력값 트리 생성
for _ in range(n-1):
    p_node, c_node, w = map(int, sys.stdin.readline().split())
    tree[p_node].append((c_node, w))
    tree[c_node].append((p_node, w))

weight1 = [0 for _ in range(n+1)]  # 루트노드로부터의 길이를 저장
dfs(1, tree, weight1)

# 찾은 가장 먼 노드를 기준으로, 제일 멀리 떨어진 루트노드 위치 탐색
start_node = weight1.index(max(weight1))
weight2 = [0 for _ in range(n+1)]  # 가장 멀리 떨어진 노드로부터의 거리 저장

# 체크리스트 초기화
for i in range(len(ch)):
    ch[i] = 0

dfs(start_node, tree, weight2)
print(max(weight2))


# BFS -------------
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100001)


def bfs(num):
    maxDist, Node = 0, num
    queue = deque()
    queue.append((num, maxDist))
    ch[num] = 1

    while queue:
        nowNode, nowDist = queue.popleft()
        for n in adj[nowNode]:
            if ch[n[0]] == 0:
                # 방문 처리
                ch[n[0]] = 1
                queue.append((n[0], n[1] + nowDist))

                # 최대값 갱신
                if maxDist < n[1] + nowDist:
                    maxDist = n[1] + nowDist
                    Node = n[0]

    return Node, maxDist


n = int(input())
adj = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for _ in range(n-1):
    tmp = list(map(int, sys.stdin.readline().split()))
    st, ed, ct = tmp[0], tmp[1], tmp[2]
    adj[st].append((ed, ct))
    adj[ed].append((st, ct))

N, D = bfs(1)

# ch 초기화
for i in range(len(ch)):
    ch[i] = 0

print(bfs(N)[1])
