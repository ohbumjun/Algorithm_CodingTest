# https://www.acmicpc.net/problem/17141

# 최초 풀이
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
이번에는 벽이 아니라
바이러스를 놓는 과정을 보여주고 있다

1) dfs 를 통해, 가능한 바이러스의 조합을 만든다
( 즉, 어디에 바이러스를 놓을 지 선택한다 )
2) 각각의 조합에 대해서 bfs를 돌린다
    단,
    기존 bfs 방식이 아니라, queue 방식으로 바이러스를 둔다
    그래서 각 단계별로, 시간을 체크해야 한다
3) 모든 bfs가 끝나고 나서,
    모든 곳에 0이 있는지 출력하고
    만약 있다면 -1을 return 한다
4) 아니라면 res (시간과 관련된 내용)을 저장하는 변수에
    측정 시간을 저장한다 
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n, m = map(int, input().split())  # n = 행,열 // m = 바이러스
a = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)


def bfs():
    bfsA = [[0]*n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            bfsA[i][j] = a[i][j]
            if bfsA[i][j] == -1:  # 바이러스를 놓은 칸
                queue.append((i, j))
    time = 1

    while queue:
        tmp = deque()
        for q in queue:
            x, y = q
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if bfsA[nx][ny] != 1:
                        bfsA[nx][ny] = -1
                        tmp.append((nx, ny))
        queue = tmp
        time += 1

    for i in range(n):
        for j in range(m):
            if bfsA[i][j] == 0:
                time = -1
                break
    return time


'''
3개가 아니라, 10개까지라도 가능해야 한다
즉, s개의 바이러스 중에서
m개를 뽑는 모든 경우의 수에 대해서
아래와 같이 진행을 해야 한다 

1) 조합
2) 각 조합의 결과에 대해서
[] 에 넣고
[]에서 for문을 돌리면서,
bfs 과정을 반복하면 된다 

'''


def dfs(L, idx, res):  # 경우의 수 구하기
    if L == m:
        vCombs.append([e for e in res])
        return
    else:
        for i in range(idx+1, len(viruses)):
            res.append(viruses[i])
            dfs(L+1, i, res)
            res.pop()


# 바이러스 위치들 조합
vCombs = []
# 먼저 바이러스 위치들을 list에 모아둔다
viruses = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            viruses.append((i, j))
dfs(0, -1, [])

for vComb in vCombs:
    for v in vComb:
        x, y = v
        a[x][y] = -1
    tmp = bfs()
    if tmp != -1:
        res = min(res, tmp)
    for v in vComb:
        x, y = v
        a[x][y] = 2

print(res if res != int(1e9) else -1)

# -------------------------------------------------
# python
'''
> '선택'을 해야 한다
1) 일부 빈칸 중에서, m개를 고르고
- 10개칸 중에서 m개 고르기 : 2 ^ 10
2) 그 다음, 바이러스가 퍼지는 시간을 계산해야 한다
- bfs : O(N^2) == 모든 칸 방문 가능 

-----------------------------------------------
1) '2'에 해당하는 칸을 만나면
후보 배열에 넣어주고 + 0으로 만들어준다 ( 실제는 빈칸 )
2) dfs 를 통해서, 가능한 조합의 수를 만들어주고
3) 조합의 수가 m개와 같다면, 거기서부터 bfs를 실시한다
4) 사실상, 최소 거리를 구하는 문제이기 때문에
dist 배열 사용하여, 각 칸 까지의 거리를 저장하고
5) 모두 저장한 이후, 다시 순회하면서 -1을 발견하게 되면
return( 즉, 그 조합은 가능하지 않은 조합이므로 무시 )
6) 그렇지 않다면, ans( 초기값 : -1 )에 넣어주면서
답을 구해간다 
'''
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
candi = []
ans = -1
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            a[i][j] = 0
            candi.append((i, j))

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
                # a[nx][ny] != 1 !! 즉, 벽이 아닌 경우는 모두 이동 가능
                # 왜 ?? 이동할 수는 있는거자나
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    # 퍼지기까지의 총 시간을 계산
    # cur 까지는 우선, 최대 걸린 시간을 산출해내야 한다
    # 그게 곧, 이번 조합에서, 바이러스가 퍼지기까지
    # 걸린 총 시간으로 환산될 수 있기 때문이다
    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    # ans 는 이제, 최소값을 넣는 것이다
    # ans가 정답이 되야 한다
    global ans
    if ans == -1 or ans > cur:
        ans = cur


def go(index, cnt):
    if index == len(candi):
        if cnt == m:
            bfs()
    else:
        '''
        여기서 궁금한 점이 있다.
        만약, x , y 에 대해서 a[x][y] = 3 이렇게 
        세팅해둔 것이

        다른 경우의 수에서 영향받으면 어떻게 하지 ?
        같은 배열을 현재 공유하고 있는 건데 ??

        아니지. 그래서 먼저 3을 대입해주고
        다시 또 해당 idx를 사용하지 않는 경우의 수에 대해
        0을 대입해주고 있는 것이다 
        '''
        x, y = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 0
        go(index+1, cnt)


go(0, 0)
print(ans)

# -------------------------------------------------
# C++
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
int ans = -1 // 불가능하면 -1을 return 해주어야 하므로 초기값을 -1로 세팅 
void bfs() {
    memset(d, -1, sizeof(d))
    queue < pair < int, int >> q
    for (int i=0
         i < n
         i++) {
        for (int j=0
             j < n
             j++) {
            if (a[i][j] == 3) { // 바이러스가 놓인칸은 3 
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
            if (a[i][j] != 1) { // 벽이 아니면 갈 수 있다 
                if (d[i][j] == -1) return // 갈수 없는 곳이 존재한다면 그냥 무시 
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
        a[x][y] = 3 // 바이러스를 놓은칸 3
        go(index+1, cnt+1)
        a[x][y] = 0 // 바이러스를 안놓음 
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
                ## 2라는 것은, 바이러스를 놓을 수 있는 '빈칸'을 의미한다 
                ## 즉, 2는, 바이러스를 놓을 수 있는 후보이기 때문에
                ## candi 에 넣기는 하되, 
                ## 실질적으로 빈칸이기 때문에, 0으로 만들어주는 것이다 
                a[i][j] = 0
                candi.push_back(make_pair(i, j))
            }
        }
    }
    go(0, 0) // 어디에 바이러스를 놓을지 검사 
    cout << ans << '\n'
    return 0
}

'''
