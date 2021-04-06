# https://www.acmicpc.net/problem/16946

# 처음 코드 : 시간 초과 --------------------------------------------------------------
import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

N, M = map(int, input().split())
Map = [list(map(int, input())) for _ in range(N)]
arr = [[0] * M for _ in range(N)]


'''
모든 벽에 대해서 해당 경우수를 수행해 봐야 한다
= Brute Force


'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    res = 1
    bfsA = [[0] * M for _ in range(N)]

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0 and bfsA[nx][ny] == 0:
                res += 1
                bfsA[x][y] = 1
                queue.append((nx, ny))
    return res


for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            arr[i][j] = 0
        else:
            arr[i][j] = bfs(i, j)

for a in arr:
    print(''.join(map(str, a)))


# 해설 : 시간 초과 --------------------------------------------------------------
'''
크게 2가지 부분으로 나뉜다
1) 각각의 벽을 빈칸으로 바꾸기 = Brute Force => O(NM)
2) 그 칸에서 이동해보기 = BFS, DFS : O(NM) => 왜 ? 최대 전체칸을 이동해볼 수 있기 때문이다 

O(NM) * O(NM) = ( O(NM) ) ^ 2  = 1000 ^ 4

시간이 오래 걸려서 이 방법으로는 불가능하다

'''
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
처음 bfs를 통해서,
그룹 정보들을 저장해야 한다

1) 지도 Map
2) check 배열
3) 몇번째 group인지를 저장하는 2차원 배열
4) 실제 그룹의 개수를 저장하는 group_size 배열 >> 유동적


1st
아직 방문하지 않았고, 0 애들에 대해서 bfs 시행
그렇다면 bfs는 어떤 식으로 이루어지는가 ??

sx, sy 라는 시작점
그리고 group_size배열  length 를 (예를 들어) g라고 한다
( 왜 g라고 하는 거지 ?? 현재 group_size 배열의 경우 , 3개 원소가 있으면
2 번 idx까지 표시될 것이고, 새로운 값이 들어가는 idx는 3이기 때문이다 )
그리고, 방문할 수 있는 모든 x,y에 대해
group[x][y] = g 라고 설정한다 


2nd
모든 점들 check, group 초기화

3rd
이제 다시 모든 점들을 일일히 방문
0이면 0 출력

아니라면
set을 설정해두고
4방향 이동하면서
group[x][y] 정보를 set에 넣어주기

그리고 4방향 다 탐색하면
set에 저장된 숫자 다 더해서 해당 값 출력


------------------------------------------------------------------
이 경우 시간복잡도는
1) DFS, BFS = O(NM)
2) 모든 정점 방문 Brute Force = O(NM)
3) 각 정점마다 상하좌우 4번만 방문 == O(4) == O(1)

==> NM + NM = O(NM)
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
group = [[-1]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
group_size = []


def bfs(sx, sy):
    g = len(group_size)
    q = deque()
    q.append((sx, sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g
                    q.append((nx, ny))
                    cnt += 1
    group_size.append(cnt)


for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            # set을 이용한 이유 ?? 왼쪽, 오른쪽 갔더니, 모두 1이라는 같은 그룹
            # 그러면, 그때는 그룹1을 한번만 고려하면 된다
            near = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans % 10, end='')
    print()


'''
C++ Code

'''
# include <iostream>
# include <vector>
# include <string>
# include <queue>
# include <set>
# include <tuple>
using namespace std
int n, m
int a[1000][1000]
bool check[1000][1000]
int group[1000][1000]
vector < int > group_size
int dx[] = {0, 0, 1, -1}
int dy[] = {1, -1, 0, 0}
void bfs(int sx, int sy) {
    int g = group_size.size()
    queue < pair < int, int >> q
    q.push(make_pair(sx, sy))
    check[sx][sy] = true
    group[sx][sy] = g
    int cnt = 1
    while (!q.empty()) {
        int x, y
        tie(x, y) = q.front()
        q.pop()
        for (int k=0
             k < 4
             k++) {
            int nx = x+dx[k]
            int ny = y+dy[k]
            if (0 <= nx & & nx < n & & 0 <= ny & & ny < m) {
                if (a[nx][ny] == 0 & & check[nx][ny] == false) {
                    q.push(make_pair(nx, ny))
                    check[nx][ny] = true
                    group[nx][ny] = g
                    cnt += 1
                }
            }
        }
    }
    group_size.push_back(cnt)
}
int main() {
    cin >> n >> m;
    for (int i=0; i < n; i++) {
        string s;
        cin >> s;
        for (int j=0; j < m; j++) {
            a[i][j] = s[j] - '0';
            check[i][j] = false;
            group[i][j] = -1; }
    }
    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            if (a[i][j] == 0 & & check[i][j] == false) {
                bfs(i, j); }
        }
    }
    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            if (a[i][j] == 0) {
                cout << 0; } else {
                set < int > near;
                for (int k=0; k < 4; k++) {
                    int x = i+dx[k];
                    int y = j+dy[k];
                    if (0 <= x & & x < n & & 0 <= y & & y < m) {
                        if (a[x][y] == 0) {
                            near.insert(group[x][y]); }
                    }
                }
                int ans = 1;
                for (int g: near) {
                    ans += group_size[g]; }
                cout << ans%10; }
        }
        cout << '\n'; }
    return 0; }
