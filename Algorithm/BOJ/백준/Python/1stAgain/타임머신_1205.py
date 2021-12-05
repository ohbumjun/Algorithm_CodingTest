
INT_MAX = int(1e9)
N, M    = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트
edges   = []
# 최단 거리 테이블 초기화
dist    = [INT_MAX] * (N + 1)

for _ in range(M):
    st,ed,cst = map(int,input().split())
    edges.append((st,ed,cst))

def bf(start) :
    dist[start] = 0
    for _ in range(N-1):
        for j in range(M):
            cur      = edges[j][0]
            nxt_node = edges[j][1]
            cost     = edges[j][2]
            # 현재 간선 거쳐서 , 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INT_MAX and dist[nxt_node] > dist[cur] + cost :
                dist[nxt_node] = dist[cur] + cost
    for j in range(M):
        cur      = edges[j][0]
        nxt_node = edges[j][1]
        cost     = edges[j][2]
        # 현재 간선 거쳐서 , 다른 노드로 이동하는 거리가 더 짧은 경우
        if dist[cur] != INT_MAX and dist[nxt_node] > dist[cur] + cost :
            return True

    return False
        
negative_cycle = bf(1)

if negative_cycle :
    print(-1)
else :
    for i in range(2, N+1) :
        if dist[i] == INT_MAX :
            print(-1)
        else :
            print(dist[i])

# 증명 ---
# n-1 번까지 반복하는 이유 : 싸이클을 가지지 않는 범위에서의, 최단거리가 가질 수 있는 경로 개수의 최대값 
# 즉, 음수 순환이 없다면, n-1 번 내에서 각 정점까지의 최단 거리가 구해져야 한다.
'''
K개의 정점이 존재한다면
시작점에서 K번째 정점까지의 최단 거리는 최대 K - 1개의 간선을 지닐 것이다.
그렇지 않다면, cycle이 존재한다는 것이다.

최단 경로 정의
- simple path
- 딱 하나만 선별할 것
--> ex) 서로 다른 2개의 경로가 같은 wegiht를 가져서 특정 정점까지 도달한다고 해보자
--> 그렇다 하더라도, 그중 하나만을 선택한다라는 것이다
--> ex) A,B 경로 모두 5의 비용으로 C 정점까지 도달, A경로는 3개 edge, B 경로는 4개 edge --> A 선택 


최단 경로 내에 포함된 간선들은
그 자체로도 shortes edge 이다
K1 --> (E1) --> K2 --> (E2) --> K3
E1, E2도 shortest edge가 된다는 것이다.
그래서 K-1개를 반복하는 것이다
매 순간 , 최종 최단 경로의 부분이 되는,
또 다른 작은 version 최단 경로들을 찾아가는 원리이다.
만약, 특정 노드까지의 최단 경로 간선 개수가 K-1보다 작으면 작은 거고 !

만약 K-1 번 반복 이후,K번째 에도 최단 경로가 relax 된다면 ,
- 해당 정점까지 가는 경로가, 유일하지 않다는 것이고, simple 하지 않다는 것이고
- 이 말은 즉슨, cycle이 존재한다는 것이고
- 그 과정에서 relax 까지 일어났다는 것이니까, negative cycle이 존재한다는 의미이다 


'''
    