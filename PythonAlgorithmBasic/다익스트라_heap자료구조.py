'''
기본 원리는 동일하다
매 단계마다, 최단 거리가 가장 짧은 노드를 선택해가면서
최단 거리 정보를 갱신한다.

1) 
다만, 매 단계에서최단 거리가 가장 짧은 노드를 선택하는 과정에서
기존과 같이 배열을 모두 탐색하는 것이 아니라,
heap 자료구조를 이용한다는 면에서 차이가 있다 .

2) 또한
방문 여부를 저장하는 visited라는 배열 없이
가능하다는 것 .

즉, 우선순위큐에서 꺼내진 노드에 대한 거리 정보
---
최단 거리 정보가 저장된 배열에 저장된 거리 정보

둘을 비교하여, 기존 최단 거리 정보 배열에 있는 정보가 더 거리가 작다면
우선순위 큐에서 꺼낸 정보는 무시한다. 

'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n , m = map( int, input().split() )
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는, 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] * ( n + 1 ) for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화(: distance[i] >> i 노드까지 가는 최단 거리 > 한번 정해지면 update 안된다 )
distance = [[INF] * ( n + 1 ) ]

# 모든 간선 정보 입력받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def dijkstra(start) :
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush( q , ( 0 ,start ) )
    distance[start] = 0

    while q : # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다
        if distance[now] < dist :
            continue 
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost 
                heapq.heappush( q, ( cost , i[0] ) )

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한 (INFINTY)라고 출력
    if distance[i] = INF :
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])

'''

다익스트라 알고리즘 시간 복잡도 : O(ElogV)

> 노드를 하나씩 꺼내 검사하는 반복문(while)은 노드의 개수 V이상의 횟수로는 처리되지 않는다
( while q :)

왜 ?? 
if distance[now] < dist :
    continue 

위의 코드를 통해서, 
해당 노드를 처리할지 안할지를 결정할 때 ,
방문하지 않은 노드들에 대해서만 수행하도록 했기 때문이다
그래서 아래의 for 반복문은, 노드의 개수만큼만 수행될 것이다 

> 현재 우선순위큐에서 꺼낸 노드와 , 연결된, 다른 노드들을 확인하는 총 횟수는
최대 간선의 개수(E)만큼 연산이 수행될 수 있다

왜 ??
각 노드에 대해서,인접한 노드들만을 확인하는 것이기 때문이다.
즉, 결과적으로 전체 연결 간선만큼만 최대로 수행되는 것이다 

for i in graph[now]:
    cost = dist + i[1]
    # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
    if cost < distance[i[0]] :
        distance[i[0]] = cost 
        heapq.heappop( q, ( cost , i[0] ) )
  
직관적으로 보자면,
위의 모든 과정은
E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 유사하다 

그렇기 때문에 
시간 복잡도를 O(ElogE)라고 판단할 수 있다

만일, 중복 간선을 포함하지 않는 경우 , 
즉, 오는 간선, 가는 간선만이 존재하는 경우

간선의 개수는 최대 노드의 개수 ^ 2

따라서 O(ElogE) > O(Elog( V ^ 2 )) > O(2ElogV) > O(ElogV) 라고 판단될 수 있다


'''

