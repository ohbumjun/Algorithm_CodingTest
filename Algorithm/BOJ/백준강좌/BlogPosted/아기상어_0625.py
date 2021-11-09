# https://www.acmicpc.net/problem/16236
'''
*  저장을 어떻게 할 것이냐
- 물고기 : 위치, 크기  ex) A[r][c] == 물고기의 크기 // 물고기가 없는 경우는 0을 넣는다 
- 상어   : 위치, 크기, 경헙치( 지금까지 먹은 물고기의 개수 -> 크기가 변하면 0으로 )
- 공간   : 물고기, 상어

* 변하는 값, 변하지 않는 값
변하지 않는 값 : 물고기위치, 물고기크기, 
변하는 값 : 상어의 위치 , 상어의 크기 

--1) 이동할 때마다, 

* 이동 ( 아래 반복 ) 
1) 상어가 먹을 수 있는 물고기를 찾고
- 거리가 가장 가까운 물고기를 먹는다 ( 격자형태에서의 최소값 = BFS , 걸리는 시간 = N^2 : 거리가 가장
가까운 상어를 찾았다고 해서, 그것이 하나는 아니니까. 즉, 상어와 물고기 사이의 '모든' 거리를 다 구해주고 
그 다음에 비로소, 최소를 찾으려고 한다 )
- 즉, 1_1) 물고기까지의 거리 , 1_2) 물고기의 위치 ( 왼쪽, 위를 먼저 먹으니까 )
2) 이동해서 먹는다 

모든 칸에 물고기가 있고, 상어가 이 물고기를 모두 먹을 수 있다면
각 칸에서, 모든 물고기까지의 거리, 위치를 파악하는 BFS를 수행

즉, BFS는 N^2
그것을 모든 격자에서 수행 N^2
따라서 O( N ^ 4 )
'''
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                # 1) 먹을 수 있는 애 : 사이즈 작은 애
                # 2) 갈수만 있는애 : 같은 애들 , 빈칸
                # 3) 그외 : 큰 애들 : x

                ok = False  # 갈 수 있냐
                eat = False  # 먹을 수 있냐
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size:  # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    ok = True
                    eat = True
                # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                elif a[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        # ans에 넣어주는 순서가 매우 중요하다
                        ans.append((d[nx][ny], nx, ny))
                        # 먹을 수 있는 물고기의 정렬 우선 순위는 다음과 같다
                        # 1) 거리
                        # 2) 행 ( 맨 위 )
                        # 3) 열 ( 맨 왼쪽)
                        # 이를 있는 그대로 반영하기 위해 위와 같은 원소의 순서로 ans에 넣어주어야 한다
    if not ans:
        return None
    ans.sort()
    return ans[0]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    x, y = nx, ny  # 아기 상어 이동 처리
print(ans)


'''
C++

#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
tuple<int,int,int> bfs(vector<vector<int>> &a, int x, int y, int size) {
    int n = a.size();
    vector<tuple<int,int,int>> ans; // "모든" 물고기까지의 거리 및 위치 정보 저장 --> "거리 , 행, 열"이 가장 낮은 물고기부터 먹어야 --> 모두 구해놓고 , 정렬 실시 
    vector<vector<int>> d(n, vector<int> (n, -1)); // 거리 배열 
    queue<pair<int,int>> q; // 큐 
    q.push(make_pair(x,y));
    d[x][y] = 0;
    while (!q.empty()) {
        tie(x,y) = q.front();
        q.pop();
        for (int k=0; k<4; k++) { // 상어가, 인접한 nx, ny로 이동하는 경우 
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && d[nx][ny] == -1) { // 범위 내에 존재 + 방문한 적이 없어야 한다 
                bool ok = false;
                bool eat = false;
                // 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if (a[nx][ny] == 0) { // 이동하려는 칸이 빈칸이면 이동하기 
                    ok = true; // 먹을수는 없으니, 이동만 할 수 있다고 해주기 
                } else if (a[nx][ny] < size) { // 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
                    ok = eat = true;
                } else if (a[nx][ny] == size) { // 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    ok = true;
                }
                if (ok) {
                    q.push(make_pair(nx,ny));
                    d[nx][ny] = d[x][y] + 1;
                    if (eat) {
                        ans.push_back(make_tuple(d[nx][ny],nx,ny)); // 먹을 수 있는 경우에만, 거리, 행 ,열. 정보를 넣어준다 
                    }
                }
            }
        }
    }
    if (ans.empty()) {
        // 먹을 수 있는 물고기가 없다면, dist를 -1 리턴해준다 
        return make_tuple(-1,-1,-1);
    }
    // 정렬 
    sort(ans.begin(), ans.end());
    // 제일 첫번째 return == 문제조건에 따라 ~ 거리 제일 작고, 행과 열도 가장 작은 것 
    return ans[0];
}
int main() {
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(n, 0));
    int x, y; // 상어의 위치 -> 계속 바뀔 수 있다 
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
            if (a[i][j] == 9) { // a[i][j]는 물고기의 크기 --> a[i][j]가 9 라는 것은, 상어가 해당 위치에 있다는 것이므로, 
                tie(x, y) = make_pair(i, j); // 상어의 위치는 별도로 저장을 하고 
                a[i][j] = 0; // 해당 위치를 0으로 만들어준다( 물고기가 없다 )
            }
        }
    }
    int ans = 0; // 시간 
    int size = 2; // 상어의 크기 
    int exp = 0;  // 경험치 ( 지금까지 먹은 물고기의 개수 )
    while (true) {
        int nx, ny, dist;
        tie(dist,nx,ny) = bfs(a, x, y, size);  // 거리, 행, 열 정보를 return 
        if (dist == -1) break;  // 더이상 먹을 수 있는 물고기가 없을 때 
        a[nx][ny] = 0;          // 해당 위치의 물고기를 먹으면 0으로 만들어준다 
        ans += dist;            // 물고기까지의 거리가, 이동거리의 합, 엄마 상어에게 도움 요청안하고 물고기 잡아먹을 수 있는 시간과 같다. 따라서, 정답에 거리를 더해주고 
        exp += 1;               // 먹은 물고기의 개수를 1 증가시켜준다 
        if (size == exp) {      // 상어 크기와 먹은 물고기의 개수가 같으면, 상어 크기를 증가시키고, 경험치 reset 
            size += 1;
            exp = 0;
        }
        tie(x,y) = make_pair(nx,ny); // 상어의 위치를 먹은 물고기의 위치로 바꿔준다 
    }
    cout << ans << '\n';
    return 0;
}


'''
