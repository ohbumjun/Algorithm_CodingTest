# https://www.acmicpc.net/problem/9376

'''

특이한 점 
- 죄수2명 == 시작점 2개
- 도착점이 없음 ( 지도의 밖)
- 문'#' : 1번 열면 계속 열려 있는 상태 -> 죄수 1명이 열면, 다른 죄수가 열지 않아도 된다 

정점 : 위치
간선 : 정점의 이동 

'''
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, x, y):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
    return dist


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = ['.'+input()+'.' for _ in range(n)]
    n += 2
    m += 2
    a = ['.'*m] + a + ['.'*m]
    d0 = bfs(a, 0, 0)
    x1 = y1 = x2 = y2 = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    d1 = bfs(a, x1, y1)
    d2 = bfs(a, x2, y2)
    ans = n*m

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                cur -= 2
            ans = min(ans, cur)
    print(ans)


# C++ 코드
'''
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>
#include <tuple>

using namespace std;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

// 시작점 다른 bfs 총 3번 진행하기 
vector<vector<int>> bfs(vector<string> &a, int x, int y) {
    int n = a.size();
    int m = a[0].size();
    vector<vector<int>> d(n, vector<int>(m));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            d[i][j] = -1;
        }
    }
    deque<pair<int,int>> q;
    q.push_back(make_pair(x, y));
    d[x][y] = 0;
    while (!q.empty()) {
        tie(x,y) = q.front(); q.pop_front();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (d[nx][ny] != -1) continue;   // 이미 방문한적 있으면 skip
            if (a[nx][ny] == '*') continue;  // 지나갈 수 없는 벽이면 skip
            if (a[nx][ny] == '#') {  // 문이라면, 지나가되, 가중치 + 1
                d[nx][ny] = d[x][y] + 1;
                q.push_back(make_pair(nx,ny));
            } else { // 일반 빈칸이면 진행 
                d[nx][ny] = d[x][y];
                q.push_front(make_pair(nx,ny));
            }
        }
    }
    return d; // 거리 정보가 담긴 2차원 배열 return 
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<string> a(n+2);

        // 판 확장하기 
        // 1. 가로 부분 확장 
        for (int i=1; i<=n; i++) { // 앞에 열 하나를 더 넣어주기 위해서 일부러 i는 1부터 시작함 
            cin >> a[i];
            a[i] = "." + a[i] + "."; // ?? a[i] 가 하나의 row 가 되는 것이다 .
        }
        n += 2;
        m += 2;
        // 2. 세로 부분 확장 
        for (int j=0; j<m; j++) {
            a[0] += ".";
            a[n-1] += ".";
        }

        vector<vector<int>> d0 = bfs(a, 0, 0);

        // 죄수들 위치 구하기 
        int x1, y1, x2, y2;
        x1 = y1 = x2 = y2 = -1;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (a[i][j] == '$') {
                    if (x1 == -1) {
                        x1 = i;
                        y1 = j;
                    } else {
                        x2 = i;
                        y2 = j;
                    }
                }
            }
        }
        vector<vector<int>> d1 = bfs(a, x1, y1);
        vector<vector<int>> d2 = bfs(a, x2, y2);

        // 공통점 찾기 
        int ans = n*m;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (a[i][j] == '*') continue;
                if (d0[i][j] == -1 || d1[i][j] == -1 || d2[i][j] == -1) continue; // 3개 모두 방문한 적이 없는 정점이면, 공통점이 될 수 없으므로 skip 
                int cur = d0[i][j] + d1[i][j] + d2[i][j];
                if (a[i][j] == '#') cur -= 2; // 공통점이 문이라면 -2 해주기 
                if (ans > cur) ans = cur;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}

'''
