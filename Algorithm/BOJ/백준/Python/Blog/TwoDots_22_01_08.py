# https://www.acmicpc.net/problem/16929

'''
< 핵심 포인트 >
- dfs 함수에서의 return False 의미
- 사이클 여부 검사하기 위한 배열의 필요성
- 방문처리 코드의 순서 

풀이 방법
- 모든 칸을 순회하면서, 사이클이 있는지를 본다.

사이클을 돌기 시작하면, 
1) 모든 정점을 돌 수 있고
2) 각 사이클 단계에서 또 모든 정점을 돈다

따라서 시간 복잡도 : O((NM)^2)
O( 2500 ^ 2) = O( 6250000 )

중간에 특정 코드를 한번 살펴보자
def go( x, y, cnt, color) : // cnt : 방문한 칸의 개수, color : 색 
    if cnt == 4 : return true
    check[x][y] = true
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m :
            # 방문 한적이 없고, 같은 색상을 지닌다면, 방문
            if check[nx][ny] == False and a[nx][ny] == color :
                if go( nx, ny, cnt + 1,, color ) :
                    return True
    // False가 나온다는 것은
    // 가능한 방문 방향 4개를 다 방문해봤는데, 크기가 4인 연속 경로가 없었다는 것
    // 이때는 False를 리턴하게 될 것이다 
    return False

위의 코드는 무슨 작업을 하는 것일까 ?? 
현재 좌표상에서, 상하좌우를 이동하면서
같은 색상을 지닌 좌표를 향해 나아가는 것이다.

그리고 그 길이가 4가 되면
즉, 연속적으로 4만큼을 이동하게 되면
true를 리턴, 아니면 false를 리턴하는 것이다 

----------------------------------------------------------------
하지만, 
위의 코드로는, "사이클" 여부를 계산할 수 없다. 

o -> o -> o -> o

이래도 위의 함수 입장에서는 true를 리턴하게 된다.
그러나, 이는 사이클이 아니다

o -> o 
^
|
o <- o

이런식으로 길이가 4라고 하더라도
다시 돌아와야 하는 것이다 

맨 마지막 위의 화살표. 가 의미하는 것은 무엇일까 ??
바로, 
" 이동가능 " + " 그 칸을 이미 방문한 경우 "

자. 4칸 "연속"해서 이동해야 하기 때문에
시작점으로부터의 "거리"를 기록해주어야 한다.

dist[x][y] 라는 배열에 '거리 정보'를 기록해 줄 것이다 

def go( x, y, cnt, color) : // cnt : 방문한 칸의 개수, color : 색 
    // 아래의 코드로 수정한다
    // 이 코드를 넣어주는 이유가 무엇일까 ?
    // o -> o 이렇게 갔는데
    // 다시 o <- o
    // 이렇게 돌아오는 경우가 있다. 
    // 그런데 이 경우는 사이클이기는 하지만, 4길이가 아니기때문에 false 처리를 해주어야 한다 
    if check[x][y] : return cnt - dist[x][y] >= 4 
    check[x][y] = true 
    dist[x][y]  = cnt

    if cnt == 4 : return true
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m :
            # 같은 색상을 지닌다면, 방문
            if  a[nx][ny] == color :
                if go( nx, ny, cnt + 1,, color ) :
                    return True
    return False


< 추가 포인트 > -------------------------------------------------------------

< 1st >
check[x][y] = true 
이 코드는 왜 go 함수를 호출하고 나서 실행되는 것일까 ??

< 2nd >
if check[nx][ny] == False and a[nx][ny] == color :
    check[x][y] = true 
    if go( nx, ny, cnt + 1,, color ) :
        return True
왜 위와 같이 표시되지 않는 것일까 ?? 

< 2nd >
와 같이 표시하게 되면, 
우리가 방문하는 모든 좌표들은
방문처리가 되버린다.

즉, check[x][y] = True, 방문 처리를 하고
go( nx, ny, cnt + 1,, color ) 방문을 하게 되는 것이다. 

그렇다면, 우리는 이미 방문 처리된 좌표를 방문하게 되는 것이다 

그런데, 우리가 필요한 것은,
어딘가를 방문했을 때, 
얘가 첫방문인지, 아니면 또 방문하는 것인지를 봐야 하는 것인데 
if check[x][y] : return cnt - dist[x][y] >= 4 

이미 다 방문처리를 해버리면 ....안된다

그래서 
1) 우선 함수 호출 먼저 하고 go( nx, ny, cnt + 1,, color )
2) 이미 방문한 칸인지 검사하고 if check[x][y] : return cnt - dist[x][y] >= 4 
3) 그 다음 방문 처리를 하는 것이다 

< 또 다른 풀이 >
칸을 연속적으로 이동한다고 했을 때, 
현재 이동 전의 칸 , 
그 다음 이동칸 ,
그런데 그 다음 이동칸이 이미 방문한 칸 

그러면 싸이클 true 처리를 해준다 

// px, py : 이전 칸
def go(x, y, px, py, color) :
    if check[x][y] : return true
    check[x][y] = true
    for i in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m :
            # 이전 칸과 다르면
            if ( nx != px and ny != py ) and a[nx][ny] == color :
                # 해당 방향으로의 싸이클이 존재한다는 것이기 때문이다 
                if go( nx, ny, x, y, color ) : return true  
return False
'''
import sys
import heapq
from collections import Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
chr = [[0] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]  # 상, 하 , 좌, 우
dy = [0, 0, -1, 1]

res = 0


def go(x, y, cnt, color):  # 기준점에서, 특정 점까지 간, "거리"
    global res
    if chr[x][y] == 1:  # 사이클 : 이미 방문한 기준점 , 다시 방문하기
        return cnt - dist[x][y] >= 4

    chr[x][y] = 1
    # dist : 출발점으로부터의 거리
    # 한번 방문한 위치에 대해서는 dist를 update해줄 일이 없을 것이다
    dist[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # chr[nx][ny] == 0 이라는 조건을 두지 않는다
        # 우선 가보고, 방문했으면, 그때에 따라서 다르게 판단하기 위해서이다
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == color:
            if go(nx, ny, cnt + 1, color):
                return True
    # 여기서 False를 return 한다는 것은, 4방향 어디에서도 싸이클을 찾지 못했다는 뜻
    return False


# main ----------------------------------
for i in range(N):
    for j in range(M):
        if chr[i][j] == 0:
            ok = go(i, j, 0, arr[i][j])
            if ok:
                print("Yes")
                exit(0)

print("No")


'''
요약 정리 :
1) 모든 정점 에 대한 싸이클 검사
- Brute Force
2) 한 정점에서 시작하여, 싸이클 검사
- DFS

'''

