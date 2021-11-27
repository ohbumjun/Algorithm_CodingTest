# https://www.acmicpc.net/problem/16947

'''
< Notion 참고 > 

문제의 조건상

순환선 == 싸이클. 이라고 해석할 수 있다 
< 정의 : '싸이클' >
'경로'인데,
'시작점, 도착점'이 같은 싸이클을 의미한다 

N개의 정점과, N - 1개의 간선으로 이루어져 있는 그래프는 '트리'이다 
'트리'의 특징 중 하나는 
'싸이클'이 없다 .라는 것이다 

그리고 이러한 '트리'에 '간선'을 1개 추가하면 
'싸이클'이 생기고
이때 '싸이클'은
1가지만 생기게 되는 것이다 

< 문제 >
모든 정점과, 순환선이
얼마나 서로 떨어져 있는가 

< 해결 과정 >
1) 순환선 ( 싸이클 ) 찾기
2) 정점과 순환선 사이의 거리 : DFS, BFS 이용하기  >> 순환선의 정점을, 모두 시작점으로 해주고, DFS, BFS 알고리즘을 이용하여, 거리를 계산하는 것이다 


그렇다면, '순환선' 및 '싸이클'은 어떻게 찾을 수 있을까 ??

1) 싸이클에 속하는 점을 시작점으로 잡는 경우 
특정 시작점을 잡고
방문할 때마다 스택에 쌓아가고
방문처리를 해준다 

그 이후 방문할 곳이 없다면, 다시 되돌아 오는데
이때 스택에서 빼준다.
이러한 과정을 반복하다

결국, 더이상 아무데도 갈곳이 없을 때,
즉, 다른 정점으로 갈 수도 없고
되돌아갈 수도 없을 때

그때 '스택'에 남아있는 값이 바로
'싸이클 및 순환선'이 되는 것이다 .

2) 싸이클에 속하지 않는 점을 시작점으로 잡는 경우 
- 현재 만난 점은 싸이클에 속하는 점
- 스택 뒤에서부터, 현재 점까지를 빼서 모아준다. == 얘네들이 싸이클에 속하는 점들 
- 현재 스택 내에서, 싸이클에 속하지 않는 점들이 남아있게 된다.


'''


import sys
import heapq
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
1) 먼저 싸이클을 생성해야 한다

check
0 : 아직 방문 안함
1 : 방문함
2 : 방문했는데 싸이클

return
x : 해당 정점이 시작점 ( 싸이클 형성 )
-1 : 싸이클 못찾음
-2 : 싸이클 찾음, 그러나 얘는 싸이클 포함 x 

'''
n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for _ in range(n):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)


def go(x, p):  # p : 이전에 방문한 정점
    # 이미 방문한 정점
    # 싸이클의 시작점이라는 의미, 해당 점을 리턴해준다 
    if check[x] == 1:
        return x
    check[x] = 1 # 방문처리 
    for node in graph[x]: # x와 연결된 모든 정점 방문하면서 방문 시도 
        if node == p: # 이전의 정점이면 skip
            continue
        res = go(node, x) # 해당 점을 기준으로 더 들어가는 재귀적 코드를 짠다.
        if res == -2: # 결과값이 -2 라는 것은, 싸이클을 찾은 것 
                      # 하지만, 현재 x와 연결된 다음 정점은, 싸이클에 포함되지 않은 것
                      # 즉, 위의 설명 그림에서 왼쪽으로 쭉 오는 과정에서
                      # 시작점 3을 다시 스택에서 찾은 이후 
                      # 해당 짖점에서 -2를 왼쪽으로 리턴해가는데
                      # 현재 그 과정속에 있게 된 것
                      # 함수 진행할 필요가 없기 때문에
                      # -2를 return 해서 종료 시키기 
            return -2
        if res >= 0:
            # x번 정점을 2로 체크해준다
            # 해당 정점을 방문했는데, 싸이클에 포함된다
            check[x] = 2
            if x == res:  #
            # return 되다가, 즉, 왼쪽으로 쭉 리턴되어 오다가
            # 시작점을 찾았더라면 ?
            # 그 지점 이후, 왼쪽부터는
            # 더이상 사이클에 포함되지 않는 점들
            # -2를 리턴해서 왼쪽으로 넘겨준다
            # 이때는 2번째로 방문된 시작점 
                return -2
            # 그게 아니라면, 어느 지점에 머무른 상태 
            else:
                return res
    # 위의 for문에 걸리지 않았더라면, 싸이클을 찾지 못한 것이므로
    # -1을 return 한다. 
    return -1


go(1, -1)

'''
각 정점에서
싸이클 까지의 거리 판단 : BFS

< 처음 생각한 방법 >
1)for문으로 모든 정점 돈다
2) check[x] == 2 라면 0
3) 아니라면,queue에 넣고 진행
dist = 1 로 세팅 
3) queue 에 있는 것을 뺀다
- 해당 정점과 연결된 정점들을 조사하면서
- check[adjNode]를 확인한다
- 2 인 정점이 있다면 dist를 출력한다
4) 다 돌고나서도 없으면 dist += 1

< 위의 과정을 진행하면 모든 정점에 대해 while문을 해주는 것 : 비효율 ?
< 개선 방법 >
- 사이클 내에 존재하는 모든 정점을 queue에 포함시킨다
- queue 내의 정점들을 돌면서, 싸이클에 포함되지 않은 정점들의
dist 정보를 현재 queue에서 꺼낸 정점의 dist + 1을 해준다
- 한번의 while문으로, 모든 정점의 , 싸이클까지의 거리 파악 가능 

'''

queue = deque()  # 싸이클에 포함된 애들 목록
dist = [-1] * (n + 1)

for i in range(1, len(check)):
    if check[i] == 2:
        dist[i] = 0
        queue.append(i)
    else:
        dist[i] = -1


while queue:
    q = queue.popleft()
    for y in graph[q]:
        if dist[y] == -1:
            queue.append(y)
            dist[y] = dist[q] + 1

for i in range(1, len(dist)):
    print(dist[i], end=' ')

'''
C++ ----
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
vector<int> a[3000];
int check[3000]; // 0: not visited, 1: visited, 2: cycle
int dist[3000];
int go(int x, int p) {
    // -2: found cycle and not included
    // -1: not found cycle
    // 0~n-1: found cycle and start index
    if (check[x] == 1) {
        return x;
    }
    check[x] = 1;
    for (int y : a[x]) {
        if (y == p) continue;
        int res = go(y, x);
        if (res == -2) return -2;
        if (res >= 0) {
            check[x] = 2;
            if (x == res) return -2;
            else return res;
        }
    }
    return -1;
}
int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int u, v;
        cin >> u >> v;
        u -= 1; v -= 1;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    go(0, -1);
    queue<int> q;
    for (int i=0; i<n; i++) {
        if (check[i] == 2) {
            dist[i] = 0;
            q.push(i);
        } else {
            dist[i] = -1;
        }
    }
    while (!q.empty()) {
        int x = q.front(); q.pop();
        for (int y : a[x]) {
            if (dist[y] == -1) {
                q.push(y);
                dist[y] = dist[x]+1;
            }
        }
    }
    for (int i=0; i<n; i++) {
        cout << dist[i] << ' ';
    }
    cout << '\n';
    return 0;
}


'''
