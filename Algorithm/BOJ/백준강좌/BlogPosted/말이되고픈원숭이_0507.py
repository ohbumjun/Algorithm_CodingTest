# https://www.acmicpc.net/problem/1600

'''
벽 부수고 이동하기와 비슷함 

bfs 를 사용하고
q에 넣는 형식은
( r, c, t ) -> t는 나이트처럼 이동한 횟수

총 경우수 : 200 ^ 2 * 30 < 10억 

'''
# 내 처음 풀이 :

from collections import deque
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
dist = [[[-1] * (K+1) for _ in range(H)] for _ in range(W)]

'''
일반 이동
- 평지만 이동

점프 :
지금까지 점프한 횟수 비교
k + 1로 가기 ( 단, 방문한 적 없어야한다 )
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dhx = [-1, -2, -2, -1, 1, 2, 2, 1]
dhy = [-2, -1, 1, 2, 2, 1, -1, -2]

dist[0][0][0] = 0

q = deque()
q.append((0, 0, 0))

while q:
    x, y, k = q.popleft()
    # 일반 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and dist[nx][ny][k] == -1:
            dist[nx][ny][k] = dist[x][y][k] + 1
            q.append((nx, ny, k))
    # 말 이동
    for i in range(8):
        nx = x + dhx[i]
        ny = y + dhy[i]
        if k < K and 0 <= nx < H and 0 <= ny < W and dist[nx][ny][k+1] == -1:
            dist[nx][ny][k+1] = dist[x][y][k] + 1
            q.append((nx, ny, k+1))

minD = min(dist[W-1][H-1])
print(minD if minD != - 1 else -1)


# 정답 코드 -------------------------------------------------------------------
# 여기서 짚고 넘어갈 포인트는, 그냥 이동, 말 이동을 한꺼번에 처리하는 개념이라는 것
dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
a = [[0]*200 for _ in range(200)]
d = [[[-1]*31 for i in range(200)] for j in range(200)]
l = int(input())
m, n = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 0
while q:
    x, y, c = q.popleft()
    for k in range(12):
        nx = x+dx[k]
        ny = y+dy[k]
        nc = c+cost[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:
                continue
            if nc <= l:
                if d[nx][ny][nc] == -1:
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx, ny, nc))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == -1:
        continue
    if ans == -1 or ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]
print(ans)


'''
C++ 코드 --- 

#include <iostream>
#include <tuple>
#include <queue>
#include <cstring>
using namespace std;
int dx[] = {0,0,1,-1,-2,-1,1,2,2,1,-1,-2}; // 인접 4방향 + 나이트처럼 이동하기 --> 따로따로 처리하는 것이 아니라, 한번에 이동하기 위해서 !! 
int dy[] = {1,-1,0,0,1,2,2,1,-1,-2,-2,-1};
int cost[] = {0,0,0,0,1,1,1,1,1,1,1,1}; // 간선의 가중치 --> ( x, y, t ) => t + cost[k] 와 같은 방식을 통해 진행하려고 한다 
int a[200][200];
int d[200][200][31];
int main() {
    int l;
    cin >> l;
    int n, m;
    cin >> m >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    memset(d,-1,sizeof(d));
    queue<tuple<int,int,int>> q;
    d[0][0][0] = 0;
    q.push(make_tuple(0,0,0));
    while (!q.empty()) {
        int x, y, c;
        tie(x,y,c) = q.front();
        q.pop();
        for (int k=0; k<12; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            int nc = c+cost[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (a[nx][ny] == 1) continue;
                if (nc <= l) {
                    if (d[nx][ny][nc] == -1) {
                        d[nx][ny][nc] = d[x][y][c] + 1;
                        q.push(make_tuple(nx,ny,nc));
                    }
                }
            }
        }
    }
    int ans = -1;
    for (int i=0; i<=l; i++) {
        if (d[n-1][m-1][i] == -1) continue;
        if (ans == -1 || ans > d[n-1][m-1][i]) {
            ans = d[n-1][m-1][i];
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
