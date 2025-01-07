# https://www.acmicpc.net/problem/14502

'''
해당 문제는 크게 2가지 부분으로 진행된다

1) 벽을 3개 세우는 부분 
> 2) 그리고 벽을 세울 때마다, 바이러스가 퍼질 수 없는 곳의 크기.
    까지 구하는 부분

총 2 부분이 존재하는 것이다


< 벽을 3개 세우는 부분 == Brute Force > ---------------------------------------

어디에 어떤 벽을 세우면, 바이러스가 얼마나 퍼지는지 '모른다'

모르기 때문에 다 해봐야 한다

즉, Brute Force 문제가 되는 것이다 . 

< 시간 복잡도 >
빈칸의 개수는 총 N * M 개 

각 칸에는 3가지 벽을 세울 수 있다. 각 칸에 대해서 3가지 경우를 모두 고려한다고 하면

O((N * M) ^ 3) 이라는 값을 얻을 수 있다. 


< 벽을 세울 때마다, 바이러스가 퍼질 수 없는 곳의 크기 == BFS, DFS > -------------

바이러스가 퍼질 수 없는 곳을 구하려면 ,

" 빈칸 개수 - 바이러스가 퍼진 칸의 개수 "를 구하면 된다  

' 바이러스가 퍼진 칸의 개수 ' 는 어떻게 구할 것인가 ??
바로, DFS, BFS 를 통해 구할 수 있다  

' 바이러스가 퍼진다 ' 라는 것은 ,
'바이러스가 있는 곳 --> 주변 정점으로 계속 퍼져나가는' 과정을 생각하면 되는 것이다 

< 시간 복잡도 >
빈칸의 최대 개수 O( NM )


결과적으로
BF      : O((NM) ^ 3)
DFS,BFS : O(NM)

=> O((NM) ^ 4)

N,M의 최댓값은, 64

따라서, 시간복잡도는 ( 2^6 )^4 == 2^24

1억 보다 작다
따라서 충분히, 진행할 수 있다 

'''
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def bfs():
    queue = deque([])

    # arr 정보를 bfsA 에 넣는다
    bfsA = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            bfsA[i][j] = arr[i][j]
            # 바이러스 찾으면 넣기
            if bfsA[i][j] == 2:
                queue.append((i, j))

    # 바이러스에 대한 bfs 진행
    res = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and bfsA[nx][ny] == 0:
                bfsA[nx][ny] = 2
                queue.append((nx, ny))

    # 바이러스의 개수 세기
    for i in range(N):
        for j in range(M):
            if bfsA[i][j] == 0:
                res += 1
    return res


# 3중 for문
for x1 in range(N):
    for y1 in range(M):
        if arr[x1][y1] != 0:
            continue
        for x2 in range(N):
            for y2 in range(M):
                if arr[x2][y2] != 0:
                    continue
                for x3 in range(N):
                    for y3 in range(M):
                        if arr[x3][y3] != 0:
                            continue

                        # 같은 곳에 벽을 세우면 안된다
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue

                        # 이제 벽세우면 되는 건가

                        arr[x1][y1] = 1
                        arr[x2][y2] = 1
                        arr[x3][y3] = 1

                        cur = bfs()

                        ans = max(ans, cur)

                        arr[x1][y1] = 0
                        arr[x2][y2] = 0
                        arr[x3][y3] = 0

print(ans)


'''
C++

#include <iostream> //
#include <queue>
using namespace std;
int n, m;
int a[10][10];  // 연구소 지도 
int b[10][10];  // 연구소 지도 << BFS 시에만 사용한다 
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int bfs() {
    // 시작 정점 넣어주기 
    queue<pair<int,int>> q;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            b[i][j] = a[i][j];
            if (b[i][j] == 2) {
                // 바이러스 발견해서 넣기 
                q.push(make_pair(i,j));
            }
        }
    }
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            // 인접 4개 정점 + 범위 내 존재 
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                // 빈칸이면, 바이러스 퍼뜨리기 
                if (b[nx][ny] == 0) {
                    b[nx][ny] = 2;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    int cnt = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            // 빈칸의 개수 세어주기  
            if (b[i][j] == 0) {
                cnt += 1;
            }
        }
    }
    return cnt;
}
int main() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    int ans = 0;
    // 6중 for문 >> Brute Force ( 재귀함수를 사용해도 된다)
    // 3개의 칸을 세워야 하고, 행 + 열.을 탐색해야 하기 때문에, 아래와 같이 진행하였다 
    for (int x1=0; x1<n; x1++) {
        for (int y1=0; y1<m; y1++) {
            if (a[x1][y1] != 0) continue; // 1번째 칸 : 벽은 빈칸에만 세울 것이다 
            for (int x2=0; x2<n; x2++) {
                for (int y2=0; y2<m; y2++) {
                    if (a[x2][y2] != 0) continue; // 2번째 칸 : 벽은 빈칸에만 세울 것이다 
                    for (int x3=0; x3<n; x3++) {
                        for (int y3=0; y3<m; y3++) {
                            if (a[x3][y3] != 0) continue; // 3번째 칸 : 벽은 빈칸에만 세울 것이다 
                            if (x1 == x2 && y1 == y2) continue; // 3개의 벽을 세울 것이고, 같은 것이 하나라도 있으면 안된다 
                            if (x1 == x3 && y1 == y3) continue;
                            if (x2 == x3 && y2 == y3) continue;

                            // bfs 전에 벽을 세워준다 
                            a[x1][y1] = 1;
                            a[x2][y2] = 1;
                            a[x3][y3] = 1;

                            // cur : 바이러스가 퍼질 수 없는 공간의 크기 
                            int cur = bfs();
                            // 최댓값 갱신 
                            if (ans < cur) ans = cur;
                            // 해당 경우에 대한 벽세우기 3번을 진행 , 다시 취소해주기 
                            a[x1][y1] = 0;
                            a[x2][y2] = 0;
                            a[x3][y3] = 0;
                        }
                    }
                }
            }
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
