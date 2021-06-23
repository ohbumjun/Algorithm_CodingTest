# https://www.acmicpc.net/problem/17822


# 첫번째 시도
import copy
import heapq as hq
import sys
from functools import reduce
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1501*1501)

N, M, T = map(int, input().split())
board = [[0]*M for _ in range(N+1)]

for i in range(N):
    board[i+1] = deque(list(map(int, input().split())))

for _ in range(T):
    x, d, k = map(int, input().split())
    # 회전시키기
    for i in range(1, N+1):
        if i % x == 0:
            k_c = k
            if d == 0:  # 시계방향 --> pop,appendleft
                while k_c > 0:
                    board[i].appendleft(board[i].pop())
                    k_c -= 1
            else:  # 반시계방향 --> popleft, append
                while k_c > 0:
                    board[i].append(board[i].popleft())
                    k_c -= 1
    # 인접한 숫자 지우기
    b_copy = copy.deepcopy(board)
    change = False
    for r in range(1, N+1):
        for c in range(M):
            same = False
            # 같은 라인
            if c == 0:
                if board[r][c] == board[r][c+1] or board[r][c] == board[r][-1]:
                    same = True
            elif 0 < c < M-1:
                if board[r][c] == board[r][c+1] or board[r][c] == board[r][c-1]:
                    same = True
            elif c == M - 1:
                if board[r][c] == board[r][c-1]:
                    same = True
            # 다른 라인
            if r == 1:
                if board[r][c] == board[r+1][c]:
                    same = True
            elif 1 < r < N:
                if board[r][c] == board[r+1][c] or board[r][c] == board[r-1][c]:
                    same = True
            elif r == N:
                if board[r][c] == board[r-1][c]:
                    same = True
            if same:
                change = True
                b_copy[r][c] = 0  # 지워준다
    # 만약 없다면
    if change == False:
        # 평균을 구한다
        avg = sum([sum(row) for row in board]) // N
        # 평균보다 큰수에서 1 빼고, 작은 수는 1 더한다
        for r in range(1, N+1):
            for c in range(M):
                if board[r][c] > avg:
                    b_copy[r][c] -= 1
                elif board[r][c] < avg:
                    b_copy[r][c] += 1
    # 변경된 정보를 board에 다시 반영한다
    board = b_copy

ans = sum([sum(row) for row in board])
print(ans)


'''
문제 해설
- 반지름이 1부터 N까지인 원판이 존재한다

i번째 원판의 j번째 수의 위치는 (i,j)이다
원판을 회전시켜야 한다

A[i][j] = i,j에 있는 수 
ex) A[1] = [1,1,2,3]


> 회전
1) 시계방향   : 오른쪽으로 밀기
2) 반시계방향 : 왼쪽으로 밀기 

'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# rotate 부분


def go(a, x, d, k):
    if d == 0:
        a[x] = a[x][-k:] + a[x][:-k]
    else:
        a[x] = a[x][k:] + a[x][:k]


def check(a):
    # 같은 수가 있으면 모두 지우고
    # 그것이 아니라면, 빼거나 더하기
    n = len(a) - 1
    m = len(a[1])

    # 해당 위치가 인접한 것과 같은지 아닌지를 판별하기 위한 true,false 배열 마련
    d = [[False]*m for _ in range(n+1)]

    ok = False  # 같은 수 있으면 true, 아니면 false
    # d[i][j] = true (같은 수), false: (같은 수 아님)

    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            # 사실상 특정 수를 기준으로, 오른쪽, 아래가 같은지만 보는 것이다
            # ? 왜 위랑, 아래는 안보는 걸까
            # 안봐도 된다. 같은 위치에 있는 애들은 true로 만들어주면 되기 때문이다
            # 즉, 이런식으로 오른쪽, 아래만 비교할 때,
            # # 맨 오른쪽은 맨 왼쪽과 비교하는 코드로 구성되어 있다( 결국은 모두 비교 가능 ) ==> a[i][(j+1) % m]
            if a[i][j] == a[i][(j+1) % m]:
                d[i][j] = d[i][(j+1) % m] = True
            if i+1 <= n and a[i][j] == a[i+1][j]:
                d[i][j] = d[i+1][j] = True

    # 같은 부분 지워주기
    for i in range(1, n+1):
        for j in range(m):
            if d[i][j]:
                ok = True
                a[i][j] = 0
    return ok

# 같은 부분 없으면, 평균 구하고, 큰것은 -1, 작은 것은 +1


def adjust(a):
    n = len(a)-1
    m = len(a[1])
    total = 0  # sum
    cnt = 0

    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            total += a[i][j]
            cnt += 1

    if cnt == 0:
        return

    for i in range(1, n+1):
        for j in range(m):
            if a[i][j] == 0:
                continue
            if total < a[i][j] * cnt:
                # total/cnt < a[i][j] (-1)
                a[i][j] -= 1
            elif total > a[i][j] * cnt:
                # total/cnt > a[i][j] (+1)
                a[i][j] += 1


n, m, t = map(int, input().split())
a = [None] + [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())
    for y in range(x, n+1, x):
        go(a, y, d, k)

    ok = check(a)

    if ok == False:
        adjust(a)


ans = sum(sum(row) for row in a[1:])
print(ans)

'''
C++

#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
void go(vector<vector<int>> &a, int x, int d, int k) {
    if (d == 0) {
        rotate(a[x].rbegin(), a[x].rbegin()+k, a[x].rend());
    } else { // d == 1
        rotate(a[x].begin(), a[x].begin()+k, a[x].end());
    }
}
bool check(vector<vector<int>> &a) {
    int n = (int)a.size() - 1;
    int m = a[1].size();
    vector<vector<bool>> d(n+1, vector<bool>(m, false));
    bool ok = false; // 같은 수 있으면 true, 아니면 false
    // d[i][j] = true (같은 수), false: (같은 수 아님)
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            if (a[i][j] == 0) continue;
            if (a[i][j] == a[i][(j+1)%m]) {
                d[i][j] = d[i][(j+1)%m] = true;
            }
            if (i+1 <= n && a[i][j] == a[i+1][j]) {
                d[i][j] = d[i+1][j] = true;
            }
        }
    }
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            if (d[i][j]) {
                ok = true;
                a[i][j] = 0;
            }
        }
    }
    return ok;
}
void adjust(vector<vector<int>> &a) {
    int n = (int)a.size() - 1;
    int m = a[1].size();
    long long sum = 0;
    long long cnt = 0;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            if (a[i][j] == 0) continue;
            sum += a[i][j];
            cnt += 1;
        }
    }
    if (cnt == 0LL) return;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            if (a[i][j] == 0) continue;
            if (sum < (long long)a[i][j]*cnt) {
                // sum/cnt < a[i][j] (-1)
                a[i][j] -= 1;
            } else if (sum > (long long)a[i][j]*cnt) {
                // sum/cnt > a[i][j] (+1)
                a[i][j] += 1;
            }
        }
    }
}
int main() {
    int n, m, t;
    cin >> n >> m >> t;
    vector<vector<int>> a(n+1, vector<int>(m));
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    while (t--) {
        int x, d, k;
        cin >> x >> d >> k;
        for (int y=x; y<=n; y+=x) {
            go(a, y, d, k);
        }
        bool ok = check(a);
        if (ok == false) {
            adjust(a);
        }
    }
    int ans = 0;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<m; j++) {
            ans += a[i][j];
        }
    }
    cout << ans << '\n';
    return 0;
}


'''
