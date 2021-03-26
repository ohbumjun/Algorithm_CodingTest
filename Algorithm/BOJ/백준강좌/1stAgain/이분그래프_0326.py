# https://sujinlee.dev/algorithms/boj-1707/

'''
이분 그래프란, 

어떤 그래프의 정점의 집합을
둘로 분할하여, 
각 집합에 속한 정점끼리는 
서로 인접하지 않도록 분할할 수 있는 그래프이다. 

다른 말로 하면,
각 간선은, 서로 다른 집합에 속한 정점들만을 연결해야 하고

같은 집합에 속한 정점들을 연결하면 안된다.

이를 푸는 대략적인 방향은,
2개의 집단을 나누기 위해서, color A, B 라고 표현하여 ( 혹은 2개의 숫자로만 표시하여 )

ex) bfs를 이용한다면
방문하는 정점은 A
그와 인접한 정점은 B 
로 색칠해간다

그러다가, 인접한 정점이, 현재 방문한 정점과 색깔이 같으면
이는 False

왜냐하면, 간선으로 연결된
인접한 정점끼리는
색이 같으면 안되기 때문이다

간선은, 서로 다른 집합, 서로 다른 색의
집합들만을 연결하는 녀석이기 때문이다 


--------------------------------------------------------
< 구체적 풀이 >
탐색 시, 현재 정점과 인접한 정점 중, 
1) 아직 방문하지 않은 정점이 있다면,
현재 정점과 다른 그룹 번호를 부여하고 
2) 이미 방문한 경우라면, 2가지
    2_1) 현재 정점과 인접 + 이미 방문 + 그룹 번호 다름 == 이분 그래프 만족 
        BFS 라면 큐에 넣을 필요가 없고 + DFS라면 함수를 재귀호출하지 않아도 된다
    2_2) 현재 정점과 인접 + 이미 방문 + 그룹 번호 같음 == 이분 그래프 불만족 
3) 모든 정점이, 서로 연결되지 않을 수도 있다.
따라서, 한번도 방문하지 않은 정점이 있을 때마다 BFS, DFS를 호출해야 한다( for문 이용하여, 모든 정점 처리 )


< 참고 >
https://peisea0830.tistory.com/m/66

bfs, dfs를 for문을 돌면서, 모든 정점에 대해 적용하는 이유 ?

모든 정점이 간선을 지니는 것이 아닐 수도 있기 때문이다 

'''

import sys
import collections

k = int(sys.stdin.readline())

for _ in range(k):
    # 정점, 간선 입력부
    v, e = map(int, sys.stdin.readline().split())

    # adj : 인접 리스트
    adj = [[] for _ in range(v + 1)]

    # label : 방문하지 않았다면 -1인 방문 확인 배열
    label = [-1] * (v + 1)

    # 그래프 입력부
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    q = collections.deque()

    ans = True

    # BFS > 간선으로 연결되지 않을 수도 있는 경우를 대비하여, 모든 정점에 대해 돈다
    for i in range(1, v + 1):
        # ans가 False이면 탈출
        if not ans:
            break
        # 아직 방문하지 않은 정점이 있다면
        if label[i] == -1:
            q.append(i)
            label[i] = 1
            # bfs 실행
            while q:
                # bfs 도중 이분 그래프라 아니라면 탈출
                if not ans:
                    break
                now = q.popleft()
                for next in adj[now]:
                    # next ,  즉, 방문할 정점이 방문하지 않았다면, 그룹 번호를 바꿔 방문
                    if label[next] == -1:
                        label[next] = (label[now] + 1) % 3
                        q.append(next)
                    else:
                        # next가 방문했으나 , 그룹번호가 같다면, 이분그래프가 아니다
                        if label[next] == label[now]:
                            ans = False

    # 정답 출력
    if ans:
        print("YES")
    else:
        print("NO")
