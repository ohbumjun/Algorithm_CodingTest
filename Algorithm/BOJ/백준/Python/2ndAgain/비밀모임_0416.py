#
# 첫번째 풀이 : 플로이드 와샬 ( 틀림  ) ---------------------------
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

for _ in range(n):
    
    node, edge = map(int, sys.stdin.readline().split() )
    dy    = [ [1001] * ( node + 1 ) for _ in range( node + 1 ) ]
    
    for e in range(edge) :
        st, ed, cost = map(int, sys.stdin.readline().split())
        dy[st][ed] = cost
        dy[ed][st] = cost

    numFriend = int(input())
    Fs = list(map(int , sys.stdin.readline().split()))

    # 각 노드에서, 다른 노드까지의 최소 거리 정보 구하기 
    for k in range( 1, node + 1 ) :
        for i in range(1, node + 1 ) :
            for j in range( 1 , node + 1 ) :
                dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j] )

    minD = 1001
    for d in range( 1 , node + 1 ) :
        sumD = dy[Fs[0]][d] + dy[Fs[1]][d]
        if sumD < minD  :
            minD = sumD
            idx = d
            
    print(idx)
'''
위의 답이 오답인 이유는 2가지이다
1) dy[i][i] = 0으로 설정하지 않은 것 
즉, 처음에는 dy[i][i]도 무한으로 설정되어 있다.
그런데, 자기에서 자기한테 가는 거리는 0으로 해야 한다

그렇지 않으면, 이후 min(dy[i][j], dy[i][k] + dy[k][j] ) 를 하는 과정에서 
다른 값이 도출될 수 있다.

예를 들어, 반복문을 거쳐오면서 dy[i][k] , dy[k][j]는 무한대보다 더 작은 값으로 update되어 왔는데
dy[i][i]는 무한대 그대로라면
dy[i][i]는 0으로 쳐져야 하는데

무한대로 남아서 
min(dy[i][j], dy[i][k] + dy[k][j] ) 의 결과로
dy[i][i]가 0 이 아니라, dy[i][k] + dy[k][j] 의 값으로 정의될 수 있기 때문이다


2) 2개의 친구 노드 > 다른 노드들까지의 거리. 가 아니라 ( 기준이, 친구들이 되는 것이 아니라 )

다른 노드들 > 2개의 친구 노드. 까지의 거리를 비교해야 하는 원리이다

물론, 사실 둘은 같은 원리이고, 뒤집어 놓은 것 뿐이다

하나의 출발 노드로부터 다른 모든 노드까지의 최단 경로
vs
모든 노드로부터 하나의 목적지 노드까지의 최단 경로

다만, 위의 코드가 틀렸다 ;; 
    for d in range( 1 , node + 1 ) :
        sumD = dy[Fs[0]][d] + dy[Fs[1]][d]
        if sumD < minD  :
            minD = sumD
            idx = d

아니.... Fs 에 배열 원소가 2개만 있는게 아닐 수도 있는데 ;;
for d in range( 1 , node + 1 ) :
            sumD = 0
            for j in range(numFriend) :
                sumD += dy[Fs[j]][d] 
            if sumD < minD  :
                minD = sumD
                idx = d

이런식으로 for문을 돌려야지 ;;


'''
    
# 두번째 풀이 : 플로이드 와샬 : 정답 ------------------------------
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

for _ in range(n):
    
    node, edge = map(int, sys.stdin.readline().split() )
    dy    = [ [1001] * ( node + 1 ) for _ in range( node + 1 ) ]

    for i in range(1, node + 1 ):
        dy[i][i] = 0
    
    for e in range(edge) :
        st, ed, cost = map(int, sys.stdin.readline().split())
        dy[st][ed] = cost
        dy[ed][st] = cost

    numFriend = int(input())
    Fs = list(map(int , sys.stdin.readline().split()))

    # 각 노드에서, 다른 노드까지의 최소 거리 정보 구하기 
    for k in range( 1, node + 1 ) :
        for i in range(1, node + 1 ) :
            for j in range( 1 , node + 1 ) :
                dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j] )

    minD = 1e9
    idx = -1
    for d in range( 1 , node + 1 ) :
        distance = 0

        for j in range(numFriend):
            distance += dy[d][Fs[j]]

        if distance < minD :
            idx = d
            minD = distance
            
    print(idx)
    

# 세번째 풀이 : 다익스트라 알고리즘 ------------------------------
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

_INF = int(1e9)

def dijks(start) :
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, ( 0, start ) )
    distance[start] = 0

    while q : # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush( q , ( cost, i[0] ) )
    
n = int(input())

for _ in range(n):
    node, edge = map(int, sys.stdin.readline().split() )
    # 각 노드에 연결되어 있는, 노드에 대한 정보를 담는 리스트 만들기
    graph = [ [] * ( node + 1 ) for _ in range( node + 1 ) ]
    # 최단 거리 테이블을 모두 무한으로 초기화 
    total_dis = [0] * ( node + 1 ) 

    # 모든 간선 정보 입력 받기 
    for e in range(edge) :
        st, ed, cost = map(int, sys.stdin.readline().split())
        graph[st].append((ed,cost))
        graph[ed].append((st,cost))

    numPp = int(input())
    Pp = list(map(int , sys.stdin.readline().split()))

    for p in Pp :
        distance = [_INF] * ( node + 1 ) 
        dijks( p )

        for i in range(len(distance)) :
            total_dis[i] += distance[i]

    # 최소 거리 출력
    minDis = _INF
    res = -1
    for idx in range(len(total_dis)) :
        if total_dis[idx] < minDis :
            minDis = total_dis[idx]
            res = idx

    print(res)
