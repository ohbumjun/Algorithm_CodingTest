# https://www.acmicpc.net/problem/2234

# Python 풀이 -----
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())  # m : 행, n : 열
a = [list(map(int, input().split())) for _ in range(m)]
group = [[-1]*n for _ in range(m)]
group_size = []
room = -1
mSize = 0


def bfs(sx, sy, room):
    group[sx][sy] = room
    q = deque()
    q.append((sx, sy))
    ans = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            if a[x][y] & (1 << k) == 0:  # 사실 이 코드가 가장 중요하다. 이렇게 simple하게 비트마스크 코드를 작성할 수 있다
                # 왜 이게 되는지 궁금하면 , 실제로 print(6 & (1<<2)) 등을 해봐라
                # 6의 1진수 버전에서, 해당 위치에 1이 존재한다면, 해당 숫자를 출력하고
                # 1이 존재하지 않는다면, 0을 출력하게 된다
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < m and 0 <= ny < n:
                    if group[nx][ny] == -1:
                        ans += 1
                        group[nx][ny] = room
                        q.append((nx, ny))
    return ans


'''
1) 이 성에 있는 방의 개수
2) 가장 넓은 방의 넓이
3) 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

서,북,동,남 --> 1,2,4,8
만약, 비트를 통해, 비교하여, 벽이 존재하지 않는다면
bfs를 통해, 같은 그룹으로 해주기 
'''

for i in range(m):
    for j in range(n):
        if group[i][j] == -1:
            room += 1
            res = bfs(i, j, room)
            group_size.append(res)

print(len(group_size))
print(max(group_size))

for x in range(m):
    for y in range(n):
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if group[nx][ny] == group[x][y]:  # 그룹정보가 같으면 skip
                continue
            s = group_size[group[nx][ny]] + group_size[group[x][y]]
            mSize = max(mSize, s)

print(mSize)


# C++ ----
'''
# include <iostream>
# include <queue>
using namespace std
int n, m
int a[50][50] // 입력값 
int d[50][50] // 방의 번호 
int room[50*50]  // room : 1번 방의 크기 
int dx[] = {0, -1, 0, 1}  // 여기서는 순서가 매우 중요 
int dy[] = {-1, 0, 1, 0}  // 서,북,동,남 == 1,2,4,8

int bfs(int x, int y, int rooms) {
    queue < pair < int, int >> q
    q.push(make_pair(x, y))
    d[x][y] = rooms
    int cnt = 0 // 방의 크기 
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
            if (d[nx][ny] != 0) continue // 방문여부 검사 
            if (a[x][y] & (1 << k)) continue // 벽 검사 --> 그 bit가 1로 세팅되어있다는 것은, 벽이라는 의미, 이동하지 않는다 
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
                // 방문하지 않은 칸에 대한 bfs
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

    // 벽 없애기 
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

'''
