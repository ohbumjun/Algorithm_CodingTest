# https://www.acmicpc.net/problem/4210
'''
< 문제 해설 >

우리가 지금까지 풀었던 문제 유형은,
시작점과 도착점이 정해져있던 유형이었다

하지만, 이 경우, 자세히 살펴보면,
여러개의 더러운 칸.
즉, 여러개의 도착점의 경우의 수가 존재한다는 것이다

1) 여러개의 도착점의 경우의 수를 구한다 : 10 팩토리얼 ( 더러운칸 10개 순열 경우 수 )
      -> 2) 매 더러운 칸 도착때마다, 시작점 update , bfs 실행 ( 10개 도착점 * (20*20)bfs )
            -> 3) 최종 최소값 찾는다 


위의 경우가 맞기는 하지만,
시간이 너무 오래 걸린다.

일반적으로 시간을 단축하는 가장 좋은 방법 중 하나는,
중복을 제거하는 것이다.

이를 기준으로 보면, 우리는 매 더러운칸을 방문할때마다
bfs를 실행한다.

하지만, 더러운 칸의 경우, 움직이지 않는다.

즉, 우리가 실행해볼 수 있는 가장 좋은 선택은,
맨처음 모든 더러운 칸에 대해 dfs를 실행하여, 해당 결과값을 저장한 이후,

그것을 이후에 반복해서 사용하는 것이다 

'''

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    b = [(0, 0)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                b[0] = (i, j)
            elif a[i][j] == '*':
                b.append((i, j))
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    for i in range(l):
        dist = bfs(a, b[i][0], b[i][1])
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue
    p = [i+1 for i in range(l-1)]
    ans = -1
    while True:
        now = d[0][p[0]]
        for i in range(l-2):
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break
    print(ans)


'''
C++ 코드

#include <iostream>
#include <algorithm>
#include <tuple>
#include <queue>
#include <string>
#include <vector>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

// sx, sy에서 시작하여, 다른 모든 칸까지의 거리 
vector<vector<int>> bfs(vector<string> &a, int sx, int sy) {
    int n = a.size();
    int m = a[0].size();
    vector<vector<int>> dist(n, vector<int>(m,-1));
    queue<pair<int,int>> q;
    q.push(make_pair(sx,sy));
    dist[sx][sy] = 0;
    while (!q.empty()) {
        int x, y;
        tie(x,y) = q.front(); q.pop();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (dist[nx][ny] == -1 && a[nx][ny] != 'x') {
                    dist[nx][ny] = dist[x][y] + 1;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    return dist;
}

int main() {
    while (true) {
        int n, m;
        cin >> m >> n;
        if (n == 0 && m == 0) break;
        vector<string> a(n);

        for (int i=0; i<n; i++) {
            cin >> a[i];
        }

        // 시작 위치, 더러운 칸의 위치를 모두 구해주기
        // 0번째 위치는 무조건 시작 위치, 나머지 더러운 칸들은,  더러운 칸의 위치로 저장 
        vector<pair<int,int>> b(1);
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (a[i][j] == 'o') { // b[0]을 세팅해두고, 이곳에는 시작위치를 넣어준다 
                    b[0] = make_pair(i,j);
                } else if (a[i][j] == '*') { // 더러운 칸을 찾으면 b 에다가 넣어주기 
                    b.push_back(make_pair(i,j));
                }
            }
        }

        // b의 개수를 기록하기 
        // d[i][j] : i번째에서 j번째로 이동하는 최소 이동 거리. 
        int l = b.size();
        vector<vector<int>> d(l, vector<int>(l));
        bool ok = true;

        for (int i=0; i<l; i++) {
            auto dist = bfs(a,b[i].first,b[i].second);
            for (int j=0; j<l; j++) {
                // dist 배열을 이용하여, 거리 정보를 저장한다 
                d[i][j] = dist[b[j].first][b[j].second];
                if (d[i][j] == -1) { // 한번이라도 못가는 경우가 있다면, 모든 더러운칸을 청소할 수 있는 경우가 없다는 것 
                    ok = false;
                }
            }
        }

        // 문제를 해결할 수 없는 경우라고 표시해주기 
        if (ok == false) {
            cout << -1 << '\n';
            continue;
        }

        // p에는 청소 순서를 넣는다 
        vector<int> p(l-1);
        for (int i=0; i<l-1; i++) {
            p[i] = i+1;
        }


        int ans = -1;
        do {
            int now = d[0][p[0]]; // 맨 처음 위치 
            for (int i=0; i<l-2; i++) {
                now += d[p[i]][p[i+1]];
            }
            if (ans == -1 || ans > now) {
                ans = now;
            }
        } while(next_permutation(p.begin(), p.end()));
        cout << ans << '\n';
    }
    return 0;
}

'''
