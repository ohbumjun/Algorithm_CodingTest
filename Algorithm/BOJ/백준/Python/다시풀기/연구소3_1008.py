# https://www.acmicpc.net/problem/17142

'''
연구소2 와 거의 유사한 문제라고 할 수 있다 

바이러스를 M개 활성 상태로 바꾸는 문제이다 

- 비활성 상태의 일부를, 활성으로 변해야 한다
- M개의 활성 바이러스로 변경한 이후, 비활성 바이러스는 
빈칸과 같은 의미를 갖게 된다 


0 : 빈칸
1 : 벽
2 : 비활성 --> 입력으로 받으면, 사실, 이 비활성 바이러스는
그냥 다 빈칸으로 가정해도 된다. 어차피 퍼지는 과정에서는
기존 비활성 바이러스가 있던 곳으로 퍼지나,
빈칸으로 퍼지나 동일하기 때문이다 


'''
# python ----
from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
candi = []
ans = -1
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            # 차이 1 (연구소 2는 a[i][j] = 0; 이 적혀있음)
            candi.append((i, j))
            a[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                q.append((i, j))
                d[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    cur = 0
    # 위까지는 동일, 하지만, 최대값을 구하는 과정에서 차이가 있다
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:  # 차이 3
                # 연구소 2 에서는 != 1 , 혹은 == 0 둘다 된다고 했다
                # 하지만, 여기서는 반드시 a[i][j] == 0 이 되어야 한다
                '''
                왜 그런 것일까 ?
                - 이 문제가 요구하는 것은
                "모든 빈칸에" 바이러스가 있게 되는 최소 시간이다. 

                즉, d[i][j] 중에서, '빈칸' 중에서의 최대값을 구해야 하는 것이다
                d[i][j]의 최대값을 구했는데, 
                그게 '비활성 바이러스'라면, 문제의 요구조건과 맞지 않는다

                따라서 a[i][j] == 0 // 빈칸
                의 조건을 반드시 만족시켜야만 한다 
                '''
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans == -1 or ans > cur:
        ans = cur


def go(index, cnt):
    if index == len(candi):
        if cnt == m:
            bfs()
    else:
        x, y = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 2  # 차이 2 --> 연구소2에서는 빈칸으로 세팅
        # 하지만, 이 문제의 경우, 비활성 중에서, 활성을 뽑아 3으로 두고
        # 그외 비활성은 2로 두고 시작해야 한다
        # 그 이유는 위에 bfs에 있다
        go(index+1, cnt)


go(0, 0)
print(ans)

# C++ ----
'''
# include <iostream>
# include <tuple>
# include <queue>
# include <cstring>
using namespace std
int a[100][100]
int d[100][100]
int dx[] = {0, 0, 1, -1}
int dy[] = {1, -1, 0, 0}
int n, m
vector < pair < int, int >> candi
int ans = -1
void bfs() {
    memset(d, -1, sizeof(d))
    queue < pair < int, int >> q
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < n
             j++) {
            if (a[i][j] == 3) {
                q.push(make_pair(i, j))
                d[i][j] = 0
            }
        }
    }
    while (!q.empty()) {
        int x, y
        tie(x, y) = q.front()
        q.pop()
        for (int k=0
             k < 4
             k++) {
            int nx = x+dx[k]
            int ny = y+dy[k]
            if (0 <= nx & & nx < n & & 0 <= ny & & ny < n) {
                if (a[nx][ny] != 1 & & d[nx][ny] == -1) {
                    d[nx][ny] = d[x][y] + 1
                    q.push(make_pair(nx, ny))
                }
            }
        }
    }
    int cur = 0
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < n
             j++) {
            if (a[i][j] == 0) {// 차이 3
                                if (d[i][j] == -1) return
                                if (cur < d[i][j]) cur = d[i][j]
                                }
        }
    }
    if (ans == -1 | | ans > cur) {
        ans = cur
    }
}
void go(int index, int cnt) {
    if (index == candi.size()) {
        if (cnt == m) {
            bfs()
        }
    } else {
        int x, y
        tie(x, y) = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 2 
        // 차이 2
        go(index+1, cnt)
    }
}
int main() {
    cin >> n >> m
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < n
             j++) {
            cin >> a[i][j]
            if (a[i][j] == 2) {
                // 차이 1 (연구소 2는 a[i][j]=0
                         이 적혀있음)
                candi.push_back(make_pair(i, j))
            }
        }
    }
    go(0, 0)
    cout << ans << '\n'
    return 0
}
'''
