# https://www.acmicpc.net/problem/6087

'''
"거울" 역할
- 방향 전환 

BFS 로 푼다 -> 최소 거리를 구하는 문제이므로 

그렇다면, 간선의 가중치는 어떻게 계산할까 ?


'''
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n = map(int, input().split())
a = [input() for _ in range(n)]
sx = sy = ex = ey = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j
dist = [[-1]*m for _ in range(n)]
q = deque()
dist[sx][sy] = 0
q.append((sx, sy))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        while 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            # dist[nx][ny]가 -1 이 아니라고, 해서 break 하면 안된다
            # [-1][0][-1]  현재 나는 오른쪽으로 가고 있는데 만일 0을 만났다 ?
            # break 하면 no. 왜냐하면, 위에서 아래로 한번 내려오면 0 자리를 방문한 것일 수도 있으므로
            # 하지만, 그 뒤에 남아있는 -1은, 계속 방문해야 하기 때문에, 계속 오른쪽으로 가야한다는 것이다
            nx += dx[k]
            ny += dy[k]
print(dist[ex][ey]-1)

'''
C++

#include <iostream>
#include <queue>
#include <tuple>
#include <string>
#include <algorithm>
using namespace std;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int main() {
    int m, n;
    cin >> m >> n;
    vector<string> a(n);
    int sx,sy,ex,ey;
    sx=sy=ex=ey=-1;

    // 'C'가 위치한 지점 정보 입력받기 
    for (int i=0; i<n; i++) {
        cin >> a[i];
        for (int j=0; j<m; j++) {
            if (a[i][j] == 'C') {
                if (sx == -1) {
                    sx = i;
                    sy = j;
                } else {
                    ex = i;
                    ey = j;
                }
            }
        }
    }

    // bfs에 시작점 넣어주기 
    vector<vector<int>> d(n, vector<int>(m, -1));
    queue<pair<int,int>> q;
    d[sx][sy] = 0;
    q.push(make_pair(sx,sy));
    while (!q.empty()) {
        int x, y;
        tie(x,y) = q.front(); q.pop();

        // 4개의 방향으로 인접하는 모든 칸을 queue에 넣어준다 
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            while (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (a[nx][ny] == '*') break; // 벽이 나오면 탈출 
                if (d[nx][ny] == -1) {       // 방문하지 않은 칸이면, 큐에 넣어주기 
                    d[nx][ny] = d[x][y] + 1;
                    q.push(make_pair(nx,ny));
                }
                
                // 여기서 중요한 것은, 방문한 칸이면, break 시켜주는 코드가 없다는 것이다
                // [-1][0][-1][-1] 이런식으로 정보가 저장되어 있는 경우가 있을수도 있다는 것. [0]의 경우는 예를 들어, 위에서 내려오면서 방문한 것일 수도 있으니까 
                nx += dx[k];
                ny += dy[k];
            }
        }
    }

    // d에는 직선의 개수를 넣었기 때문에 1을 빼면 된다 
    cout << d[ex][ey]-1 << '\n';
    return 0;
}

'''
