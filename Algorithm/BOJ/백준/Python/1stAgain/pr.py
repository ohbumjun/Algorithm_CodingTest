import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
그러면, 특정 정점까지 최소거리로 간다고 했을 때
2가지 경우가 있을 수 있다
1) 벽을 부수고 가지 않았을 때
2) 벽을 부수고 았을 때

또한, 우리는 어떤 벽을 부술 때
최소인지 모르기 때문에

모든 벽을 부숴버고, 그 벽을 부쉈을 때의
정점을 생각해보면 되는 것이다

즉,
1) brute force를 통해서, 모든 경우에서 벽을 부숴본다
2) 각 경우에 대해서, d[n][m]까지 가보는데
여기서 우리는 정점의 정보를 2개로 표시할 것이다

1) d[n][m][0] : 벽을 부수고 가지 않았을 때
2) d[n][m][1] : 벽을 부수고 갓을 때

3) 그렇다면, 여기서 더 추가적으로 고려해야 하는 것은 ,
벽을 한개까지만 부술 수 있다는 것이다

즉,
- 빈칸 -> 빈칸 ( 언제든지 가능 )
- 벽 -> 빈칸 ( 언제든지 가능 )
- 빈칸 -> 벽 ( 한번도 부수지 않았을 때 가능 )
- 벽 -> 벽 ( 불가능 )
'''
N, M = map(int, input().split())  # N : 행 , M : 열
arr = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
res = [int(1e9), int(1e9)]

d = [[[-1]*2 for _ in range(M)] for _ in range(N)]
q = deque()
q.append((a, b, c))
d[a][b][c] = 0
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 빈칸으로 이동하기
            if arr[nx][ny] == 0 and d[nx][ny][z] == -1:
                d[nx][ny][z] = d[nx][ny][z] + 1
                q.append((nx, ny, z))
            # 빈칸에서 벽으로 이동하기
            if z == 0 and arr[nx][ny] == 1 and d[nx][ny][z+1] == -1:
                d[nx][ny][z+1] = d[nx][ny][z] + 1
                q.append((nx, ny, z+1))
print(d[N-1][M-1])
return d


for i in range(N):
    for j in range(M):
        dist = None
        if arr[i][j] == 0:
            dist = bfs(i, j, 0)
        elif arr[i][j] == 1:
            dist = bfs(i, j, 1)

        if dist[N-1][M-1][0] != -1:
            res[0] = min(res[0], dist[N-1][M-1][0])
        if dist[N-1][M-1][1] != -1:
            res[1] = min(res[1], dist[N-1][M-1][1])

if res[0] == int(1e9) and res[1] == int(1e9):
    print(-1)
else:
    print(min(res))
    print(res)
