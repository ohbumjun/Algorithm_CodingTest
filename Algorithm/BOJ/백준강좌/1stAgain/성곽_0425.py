#

# Python 풀이 -----
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]


def bfs(x, y, rooms):
    q = deque()
    q.append((x, y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] != 0:
                continue
            if (a[x][y] & (1 << k)) > 0:
                continue
            q.append((nx, ny))
            d[nx][ny] = rooms
    return cnt


rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i, j, rooms)))
print(rooms)
ans = 0
for i in range(1, rooms+1):
    if ans < room[i]:
        ans = room[i]
print(ans)
ans = 0
for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == d[x][y]:
                continue
            if (a[x][y] & (1 << k)) > 0:
                if ans < room[d[x][y]]+room[d[nx][ny]]:
                    ans = room[d[x][y]]+room[d[nx][ny]]
print(ans)

# C++ ----
# include <iostream>
# include <queue>
using namespace std
int n, m
int a[50][50]
int d[50][50]
int room[50*50]
int dx[] = {0, -1, 0, 1}
int dy[] = {-1, 0, 1, 0}
int bfs(int x, int y, int rooms) {
    queue < pair < int, int >> q
    q.push(make_pair(x, y))
    d[x][y] = rooms
    int cnt = 0
    while (!q.empty()) {
        x = q.front().first
        y = q.front().second
        q.pop()
        cnt += 1
        for (int k=0
             k < 4
             k++) {
            int nx = x+dx[k]
            int ny = y+dy[k]
            if (nx < 0 | | nx >= n | | ny < 0 | | ny >= m) continue
            if (d[nx][ny] != 0) continue
            if (a[x][y] & (1 << k)) continue
            q.push(make_pair(nx, ny))
            d[nx][ny] = rooms
        }
    }
    return cnt
}
int main() {
    cin >> m >> n
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < m
             j++) {
            cin >> a[i][j]
        }
    }
    int rooms = 0
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < m
             j++) {
            if (d[i][j] == 0) {
                rooms += 1
                room[rooms] = bfs(i, j, rooms)
            }
        }
    }
    cout << rooms << '\n'
    int ans = 0
    for (int i=1
         i <= rooms
         i++) {
        if (ans < room[i]) {
            ans = room[i]
        }
    }
    cout << ans << '\n'
    ans = 0
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < m
             j++) {
            int x = i
            int y = j
            for (int k=0
                 k < 4
                 k++) {
                int nx = x+dx[k]
                int ny = y+dy[k]
                if (nx < 0 | | nx >= n | | ny < 0 | | ny >= m) continue
                if (d[nx][ny] == d[x][y]) continue
                if (a[x][y] & (1 << k)) {
                    if (ans < room[d[x][y]]+room[d[nx][ny]]) {
                        ans = room[d[x][y]]+room[d[nx][ny]]
                    }
                }
            }
        }
    }
    cout << ans << '\n'
    return 0
}
