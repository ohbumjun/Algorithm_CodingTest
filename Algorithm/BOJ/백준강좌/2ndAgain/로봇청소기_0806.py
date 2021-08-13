# https://www.acmicpc.net/problem/4991


'''
< 문제 해설 > -

우리가 지금까지 풀었던 문제 유형은,
시작점과 도착점이 정해져있던 유형이었다

하지만, 이 경우, 자세히 살펴보면,
여러개의 더러운 칸.
즉, 여러개의 도착점의 경우의 수가 존재한다는 것이다

1) 여러개의 도착점의 경우의 수를 구한다 : 10 팩토리얼 ( 더러운칸 10개 순열 경우 수 )
      -> 2) 매 더러운 칸 도착때마다, 시작점 update , 해당 더러운 칸을 기준으로 또 다시 bfs 실행 ( 10개 도착점 * (20*20)bfs )
            -> 3) 최종 최소값 찾는다 


위의 경우가 맞기는 하지만,
시간이 너무 오래 걸린다.

일반적으로 시간을 단축하는 가장 좋은 방법 중 하나는,
중복을 제거하는 것이다.

이를 기준으로 보면, 우리는 매 더러운칸을 방문할때마다
bfs를 실행한다.

하지만, 더러운 칸의 경우, 움직이지 않는다.

-----------------------------------------------------------------

즉, 우리가 실행해볼 수 있는 가장 좋은 선택은,
맨처음 모든 더러운 칸에 대해 dfs를 실행하여, 해당 결과값을 저장한 이후,

그것을 이후에 반복해서 사용하는 것이다 

따라서, 시작점 + 더러운점. 을 기준으로 모든 bfs를 실행한 다음, 
그 해당 결과를 어디엔가 저장해둔다  

'''
import sys
import heapq
import math
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(maps, sx, sy):
    d = [[-1]*w for _ in range(h)]
    d[sx][sy] = 0
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if d[nx][ny] == -1 and maps[nx][ny] != 'x':
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
    return d

# 1,2,3 // 1,3,2 // 1,2,3 --> 서로 다른 조합의 수 구하는 코드 
# 어떻게 이걸 구하냐 !!
# 1,2,3,4 --> 더러운 공간 (명칭)
# 모든 애들 : 내림차순 될때까지 반복 
# 1 2 3 4  --> 4 3 2 1 
# 1 2 3 4 --> 1 2 4 3 
# 1 2 4 3 --> 1 3 4 2 --> 1 3 2 4
# 4,3,2,1 --> 
def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i] <= arr[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr) - 1
    while j > 0 and arr[j] <= arr[i-1]:
        j -= 1
    arr[j], arr[i-1] = arr[i-1], arr[j]
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True


while True:
    w, h = map(int, input().split())
    ans = -1
    if w == 0 and h == 0:
        break
    maps = [list(input()) for _ in range(h)]
    places = [0] # 깨끗 + 더러운 칸 
    # 위치 찾기
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'o':
                places[0] = (i, j)
            if maps[i][j] == '*':
                places.append((i, j))
    d = [[0]*len(places) for _ in range(len(places))]
    # 특별한 칸 i 에서, 특별한 칸 j 까지의 거리 구하기 ( 특별한 칸 : places )
    # d[i][j] 
    ok = True
    for i in range(len(places)):
        sx, sy = places[i][0], places[i][1] # 0,0 // 1,1 // 2,2
        dist = bfs(maps, sx, sy)
        for j in range(len(places)):
            nx, ny = places[j][0], places[j][1]
            d[i][j] = dist[nx][ny] # 0,0 ~ 1,1 까지의 거리 
            if d[i][j] == -1: # 방문 x --> -1
                ok = False
    if ok == False:
        print(-1)
        continue
    # 이제 경우의 수들을 구해주면서, 최소 거리값을 구해가야 한다
    # p : ex) 1,2,3,4 --> 4,3,2,1 ( while --> 각 조합에 대한 최소 거리 )
    p = [x for x in range(1, len(places))] # 1,1, // 2,2, // 3,3  ---> 3,3 // 2,2 // 1,1 
    while True:
        tmp = d[0][p[0]]
        for i in range(len(p)-1):
            tmp += d[p[i]][p[i+1]]
        if ans == -1 or tmp < ans:
            ans = tmp
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

// sx, sy에서 시작하여, 다른 모든 칸까지의 거리를 2차원 배열 형태로 리턴해주기 
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

        // b의 개수( 시작점 + 더러운 위치 )를 기록하기 
        // d[i][j] : i번째( 시작점 + 더러운 위치 )에서 j번째( 시작점 + 더러운 위치 )로 이동하는 최소 이동 거리. 
        int l = b.size();
        vector<vector<int>> d(l, vector<int>(l));
        bool ok = true;

        // d : bfs의 모든 결과를 모아놓은 2차원 배열 
        for (int i=0; i<l; i++) {

            // i번째에서 다른 위치로 가는 거리를 구하기 위해 i번째에서 bfs를 수행한다 
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
            p[i] = i+1; // 0번칸 빼고 , 청소 순서 넣기 ( 0번칸은 시작 칸이기 때문이다 )
        }


        int ans = -1;
        do {
            int now = d[0][p[0]]; // 맨 처음 위치에서, p[0]으로 가기( 특정 더러운 위치 )
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
