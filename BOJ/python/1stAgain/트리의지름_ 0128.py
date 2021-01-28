# 트리의 지름
# https://www.acmicpc.net/problem/1967

'''
알고리즘의 이해

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
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

def dfs( start, tree, weight, ck ) :
    # start : 스타트 노드
    # tree : 우리가 순회하는 트리
    # weight : 우리가 저장할 weight 배열
    # ck : ck를 통해, 루트1번에서 시작한 건지, 최장길이 노드를 루트로 한건지 판단
    # ck가 필요한 이유는, start가 1번 트리이면, weight[start]에 어떤 값도 저장되어 있지 않으므로 setting
    # 루트노드에서 가장 멀리 떨어진 말단 노드를 탐색하고 나면, 그때의 weight[start]는 이미
    # 루트노드에서, 해당 말단 노드까지의 가중치 합이 더해진 상태이므로, 아래 if 문 설정 없이 별도 진행 가능
    if ck == 1:
        weight[1] = 0 # 루트 1번 노드 가중치 0으로 설정

    for node , w in tree[start] :
        if( weight[node]  == 0 ):
            weight[node] = weight[start] + w
            dfs( node, tree, weight, ck )

n = int(sys.stdin.readline())
tree = [ [] for _ in range(n+1) ]

# 입력값 트리 생성
for _ in range(n-1):
    p_node , c_node , w = map(int,sys.stdin.readline().split())
    tree[p_node].append((c_node,w))
    tree[c_node].append((p_node,w))

weight1 = [ 0 for _ in range(n+1)] # 루트노드로부터의 길이를 저장
dfs(1, tree, weight1, 1 )

# 찾은 가장 먼 노드를 기준으로, 제일 멀리 떨어진 루트노드 위치 탐색
start_node = weight1.index(max(weight1))

weight2 = [ 0 for _ in range(n+1) ] # 가장 멀리 떨어진 노드로부터의 거리 저장

dfs( start_node , tree, weight2 , 2 )


print(max(weight2))   