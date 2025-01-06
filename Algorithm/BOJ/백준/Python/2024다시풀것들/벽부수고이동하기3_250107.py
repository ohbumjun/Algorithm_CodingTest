# https://www.acmicpc.net/problem/16933
import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

# flag 변수를 두고
# 이동하지 않는 경우에 대해서도 dx, dy를 설정
'''
벽 부수고 이동하기 2와 동일한 원리

다만, '머무르기' 라는 선택지가 추가된 것이다

그렇다면, 벽 부수고 이동하기2 에서 추가적으로 고려할 사항은
1) 벽을 이동하되, 낮에만 이동 ==> 낮일 때 !! 라는 추가적인 고려사항을 정의
2) 밤,낮만 바뀌되, 위치는 그대로 머무는 경우 

'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, z):
    '''
    빈칸 > 빈칸 (o)
    벽   > 빈칸 (o)
    빈칸 > 벽 (경우)
    벽   > 벽 (경우)

    만약, 밤이라면, 현재 자기 자신을 다시 queue에 넣으면 되고
    낮이라면, 주변으로 이동하고 
    '''
    Night = 0  # 낮 : 0 , 밤 : 1 > 이동가능
    queue = deque([(x, y, z, Night)])
    while queue:
        x, y, z, isN = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue
            # 벽 > 빈칸, 빈칸 > 빈칸
            if arr[nx][ny] == 0 and dist[nx][ny][z][1-isN] == 0:
                dist[nx][ny][z][1-isN] = dist[x][y][z][isN] + 1
                queue.append([nx, ny, z, 1 - isN])
            # 낮이면서, 벽으로 이동
            if z < K and isN == 0 and arr[nx][ny] == 1 and dist[nx][ny][z+1][1-isN] == 0:
                dist[nx][ny][z+1][1-isN] = dist[x][y][z][isN] + 1
                queue.append([nx, ny, z+1, 1 - isN])
        # 제자리에 머무르기
        if dist[x][y][z][1-isN] == 0:
            dist[x][y][z][1-isN] = dist[x][y][z][isN] + 1
            queue.append([x, y, z, 1 - isN])


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[[[0] * 2 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

# 이제 4차원 배열
# 즉, 정점의 정의.가 달라졌기 때문에, 그에 맞춰서 다른 정점의 정의를 할당하는 것이다
dist[0][0][0][0] = 1

bfs(0, 0, 0)

res = -1
for i in range(1, K+1):
    for j in range(2):
        if dist[N-1][M-1][i][j] == 0:
            continue
        if res == -1:
            res = dist[N-1][M-1][i][j]
        elif res > dist[N-1][M-1][i][j]:
            res = dist[N-1][M-1][i][j]

print(res)


'''
C++ 코드

#include <iostream>
#include <queue>
#include <cstdio>
#include <tuple>
#include <cstring>
using namespace std;
int a[1000][1000];
int d[1000][1000][11][2];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int main() {
    int n, m, l;
    scanf("%d %d %d",&n,&m, &l);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            scanf("%1d",&a[i][j]);
        }
    }
    queue<tuple<int,int,int,int>> q;
    d[0][0][0][0] = 1;
    q.push(make_tuple(0,0,0,0));
    while (!q.empty()) {
        int x, y, z, night;
        tie(x,y,z, night) = q.front(); q.pop();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (a[nx][ny] == 0 && d[nx][ny][z][1-night] == 0) {
                d[nx][ny][z][1-night] = d[x][y][z][night] + 1;
                q.push(make_tuple(nx,ny,z,1-night));
            }
            if (night == 0 && z+1 <= l && a[nx][ny] == 1 && d[nx][ny][z+1][1-night] == 0) {
                d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1;
                q.push(make_tuple(nx,ny,z+1,1-night));
            }
        }
        if (d[x][y][z][1-night] == 0) {
            d[x][y][z][1-night] = d[x][y][z][night] + 1;
            q.push(make_tuple(x,y,z,1-night));
        }
    }
    int ans = -1;
    for (int j=0; j<2; j++) {
        for (int i=0; i<=l; i++) {
            if (d[n-1][m-1][i][j] == 0) continue;
            if (ans == -1) {
                ans = d[n-1][m-1][i][j];
            } else if (ans > d[n-1][m-1][i][j]) {
                ans = d[n-1][m-1][i][j];
            }
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
