# https://www.acmicpc.net/problem/16948
'''

자. 문제를 풀기 전에, 어떠한 방식으로 풀어야 하는지를 살펴봐야 한다

1) 간선의 가중치가 모두 1로 동일
2) 시작점에서 도착점까지의 '최소거리'

즉, "최소 이동 횟수"를 
구하는 문제라고 생각할 수 있는 것이다 

'''
from collections import deque
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
dist = [[-1]*200 for _ in range(200)]
n = int(input())
sx, sy, ex, ey = map(int, input().split())
q = deque()
q.append((sx, sy))
dist[sx][sy] = 0
while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
print(dist[ex][ey])

'''
< C++ >
#include <iostream>
#include <tuple>
#include <cstring>
#include <queue>
using namespace std;
int dx[] = {-2,-2,0,0,2,2};
int dy[] = {-1,1,-2,2,-1,1};
int dist[200][200];
int main() {
    int n;
    cin >> n;
    int sx,sy,ex,ey;
    cin >> sx >> sy >> ex >> ey;
    memset(dist,-1,sizeof(dist));
    dist[sx][sy] = 0;
    queue<pair<int,int>> q;
    q.push(make_pair(sx,sy));
    while (!q.empty()) {
        int x, y;
        tie(x, y) = q.front(); q.pop();
        for (int k=0; k<6; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                if (dist[nx][ny] == -1) {
                    q.push(make_pair(nx,ny));
                    dist[nx][ny] = dist[x][y] + 1;
                }
            }
        }
    }
    cout << dist[ex][ey] << '\n';
    return 0;
}


'''
