#

'''
BFS 알고리즘의 목적 
= 한 정점에서 시작해서, 모든 정점을 방문 

보통, DFS, BFS 둘다를 통해
한정점에서, 모든 정점을 방문하는 시도를 할 수 있다.

하지만
"최단거리" 의 경우는,
"BFS"만이 가능하다 

그리고 "모든 가중치가 1"이면
"최단 거리" 알고리즘이 된다 

"구현"과정에서 가장 중요한 것은
큐에 넣을 때, 
"방문" 처리를 해주는 것이다 

1) 간선의 가중치 '1'
2) '최소' 거리 표현
3) 그래프 표현

next[x] 
=> 주사위를 통해, 도착한 칸이 'X' 일때 
이동해야 하는 칸 

1) 일반칸    ?
2) 사다리칸  y ( x -> y 로 간다고 했을 때, y를 넣어주기 : 더 큰번호로 )
3) 뱀칸      y : 더 작은 번호로 

여기서 주로 고려해야 할 사항은 크게 2가지이다

1) 특정 칸에 대해서, 
방문 표시를 하면 안된다는 점 
2) x -> y -> next[y] ( next[y]는, y 정점에 갈때, 최종 도착 칸)
의 경로를 따를 때, 
y가 아닌, next[y]를 기준으로 판단해야 한다는 것
ex) 3 -> 5 -> 48
즉, 3에서 5로 갔는데, 사다리여서 48에 도착한다면 
48 이라는 칸이 '최종 도착 상태' 이기 때문에 
48 이라는 칸을, 기준으로 
생각해야 한다는 것이다 

즉, 우리는 x에서 바로 next[y]로 이동했다고 생각해야 한다는 것이다 

'''

from collections import deque

n,  m = map(int, input().split())
after = list(range(101))
dist = [-1] * 101
for _ in range(n + m):
    x, y = map(int, input().split())
    after[x] = y
'''
여기서, 사다리, 뱀에 대한 처리를
일반 칸에 대한 처리와 다르지 않게 
통일해준 것이라고 할 수 있다

즉, 
각종 예외 상황을 제거해버리기 위해서
사다리 , 뱀 에 대한 처리를
따로 생각하는 것이 아니라,

일반칸, 사다리, 뱀
을 한꺼번에 통일되게 생각한 것이다 
'''

dist[1] = 0  # dist[x] : x 칸까지의 최소 주사위 던진 횟수
q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in range(1, 6 + 1):
        y = x + i
        if y > 100:
            continue
        y = after[y]  # y가 아니라, 바로 after[y]로의 이동 진행
        if dist[y] == -1:  # 해당 y 좌표를 방문한 적이 없다면
            dist[y] = dist[x] + 1
            q.append(y)
print(dist[100])

'''
C++

#include <iostream>
#include <algorithm>
#include <queue>
#define next _next
using namespace std;
int dist[101];
int next[101];
int main() {
    int n, m;
    cin >> n >> m;
    for (int i=1; i<=100; i++) {
        next[i] = i;
        dist[i] = -1;
    }
    while (n--) {
        int x, y;
        cin >> x >> y;
        next[x] = y;
    }
    while (m--) {
        int x, y;
        cin >> x >> y;
        next[x] = y;
    }
    dist[1] = 0;
    queue<int> q;
    q.push(1);
    while (!q.empty()) {
        int x = q.front(); q.pop();
        for (int i=1; i<=6; i++) {
            int y = x+i;
            if (y > 100) continue;
            y = next[y];
            if (dist[y] == -1) {
                dist[y] = dist[x] + 1;
                q.push(y);
            }
        }
    }
    cout << dist[100] << '\n';
    return 0;
}

'''


# 문제가 되는 코드 1
# 뱀, 사다리 > next[x] = y
# 일반 칸 : next[x] = -1
# 이렇게 저장하고 나면, 어떤 문제가 발생할까 ?

while(!q.empty()){
    int x = q.front(); q.pop();
    for(int i=0; i <= 6; i++){
        int y = x + i;
        if(y > 100): continue;

        # y가 뱀의 시작 혹은 사다리의 시작
        # 뱀 혹은 사다리의 끝을 방문한 적이 없을 때
        if(next[y] != -1 & & dist[next[y]] == -1){
            # 뱀 또는 사다리를 타고 이동한다
            y = next[y]
        }
        if(dist[y] == -1){
            # 방문하지 않았다면, 방문하는 것이다
            dist[y] = dist[x] + 1;
            q.push(y)
        }
    }
}

'''
if(next[y] != -1 && dist[next[y]] == -1){
    # 뱀 또는 사다리를 타고 이동한다
    y = next[y]
}

위의 경우가 문제가 된다. 
현재 3에 위치하여 있고
5 -> 7 에 있는 경우를 생각해보자 

7은 이미 방문한 적이 있을 수도 있다
2 -> 7

따라서, 3에서 5로 이동할때, 
5 -> 7 로의 이동 경우가 고려되지 않을 수도 있다

왜냐하면, 7은 이미 방문처리되어
5 -> 7 경우가 고려되지 않을 수도 있다

dist[next[y]] == -1
라는 코드를 넣은 이유가 ,

무언가 BFS이니까
방문처리를 해줘야 할 것 같아서
위와 같이, 처리해준 것일 수도 있다 

그런데, 사실
게임 관점으로 보면
x -> next[y]로 바로 간 것이다
최종 도착 상태가 next[y]니까

즉, 중간에 y를 들렸는지 안들렸는지는
사실 중요하지 않은 것이다

헷갈릴 수 있는데 ,
dist(next[y])라는 코드에는
'y'라는 요인이 고려되는 것인데,
그러면 안된다는 것이다 

정리하자면,
최종점이 아니면
방문하면 안된다 

'''

# 문제가 되는 코드 2
while(!q.empty()){
    int x = q.front(); q.pop();
    for(int i=0; i <= 6; i++){
        int y = x + i;
        if(y > 100): continue;
        # y가 뱀의 시작 혹은 사다리의 시작
        # 뱀 혹은 사다리의 끝을 방문한 적이 없을 때
        if(next[y] != -1 & & dist[next[y]] == -1){
            # 뱀 또는 사다리를 타고 이동한다
            dist[next[y]] = dist[x] + 1;

            # 중간정점도 방문하고, 거리 계산해준다
            # !! 문제다. 최종점이 아니면, 방문처리를 해주어서는 안되는데
            # 여기에서 방문처리를 해줘버렸다
            dist[y] = dist[x] + 1;
            q.push(next[y])
        }else{
            # 일반 칸일 때
            if(dist[y] == -1) dist[y] = dist[x] + 1;
            q.push(y); }
    }
}

'''
언제 문제가 생기는 것일까 ??

ex) 
7 -> 8
14 -> 4

1에서 시작하여
2, 3, 4, 5, 6, 7 을 간다고 하면
결과적으로 7은 바로 8로 가기 때문에

1 -> {2, 3, 4, 5, 6, 7}이 나오게 된다

1 이 끝나고, 그 이후의 숫자들에 대해서
방문을 처리하려고 한다고 해보자 
2,3,4,5,6 같은 경우는 이미 위의 1에서 방문해버렸기 때문에
3 -> 9
4 -> 10
5 -> 11
6 -> 12

다 돌아서, 
8로 왔다고 해보자 
8에서는 13만 방문할 수 있다
왜 ? 최종 도착 칸외에는
방문처리를 원래 해주어서는 안되기 때문이다 


그런데, 코드상으로는 
8 -> {13, 14} 가 가능하다 

14는 가면 안된다
사다리를 통해 4라는 곳으로
최종 도착칸이 설정되기 때문이다

하지만, 현재 코드상으로
dist[next[14]] == dist[4] >> != -1 로 설정되어서
if문에 걸리지 못하고
else문에서 처리된다

이러한 문제가 있다는 것이다 
'''
