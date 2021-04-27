# https://www.acmicpc.net/problem/11048

# 1) Bottom - Up ( 통과 )
# 1_1) 혼자 풀이
from collections import deque
import math
import heapq
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
d[i][j]
== i,j 번째 idx 까지 왔을 때, 먹을 수 있는
사탕의 최댓값 
'''

n, m = map(int, input().split())
# n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = a[0][0]
# 행
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + a[i][0]
# 열
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + a[0][i]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + a[i][j]

print(dp[n-1][m-1])

# 1_2) 백준 풀이
n, m = map(int, input().split())
# (전제 조건 : 모든 a[x][y]는 0보다 크기때문에 가능)
# 코드상의 편리를 위해, 0번째 행, 0번째 열을, 모두 0을 값으로 넣어 초기화
a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1])+a[i][j]
print(d[n][m])

'''
#include <cstdio>
#include <algorithm>
using namespace std;
int a[1001][1001];
int d[1001][1001];
int max3(int x, int y, int z) {
    return max(x, max(y, z));
}
int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            scanf("%d",&a[i][j]);
        }
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            d[i][j] = max3(d[i-1][j],d[i][j-1],d[i-1][j-1])+a[i][j];
        }
    }
    printf("%d\n",d[n][m]);
    return 0;
}

'''

# 2) 가능 방법
# bottom-up이, 이전 칸에서 오는 방식이었다면
# 3번째 방법은, 현재 칸에서, 다음칸으로 가는 방식을 취한다
n, m = map(int, input().split())
a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
d[1][1] = a[1][1]
# 참고 : 2번째 방법과 3번째 방법에서 d[i][j]에 들어있는 값은 동일하다
# 그저, 점화식을 채우는 방식만 바뀔 뿐인 것이다
for i in range(1, n+1):
    for j in range(1, m+1):
        if j+1 <= m and d[i][j+1] < d[i][j] + a[i][j+1]:
            d[i][j+1] = d[i][j] + a[i][j+1]
        if i+1 <= n and d[i+1][j] < d[i][j] + a[i+1][j]:
            d[i+1][j] = d[i][j] + a[i+1][j]
        if i+1 <= n and j+1 <= m and d[i+1][j+1] < d[i][j] + a[i+1][j+1]:
            d[i+1][j+1] = d[i][j] + a[i+1][j+1]
print(d[n][m])

'''
#include <cstdio>
#include <algorithm>
using namespace std;
int max3(int x, int y, int z) {
    return max(x, max(y, z));
}
int a[1001][1001];
int d[1001][1001];
int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            scanf("%d",&a[i][j]);
        }
    }
    d[1][1] = a[1][1];
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            // -> 
            if (j+1 <= m && d[i][j+1] < d[i][j] + a[i][j+1]) {
                d[i][j+1] = d[i][j] + a[i][j+1];
            }
            // 아래
            if (i+1 <= n && d[i+1][j] < d[i][j] + a[i+1][j]) {
                d[i+1][j] = d[i][j] + a[i+1][j];
            }
            // 대각선 아래 오른쪽
            if (i+1 <= n && j+1 <= m && d[i+1][j+1] < d[i][j] + a[i+1][j+1]) {
                d[i+1][j+1] = d[i][j] + a[i+1][j+1];
            }
        }
    }
    printf("%d\n",d[n][m]);
    return 0;
}

'''

# 3) 3번째 방법
# 여기서는, 그저 대각선을 가는 방법이 사실 의미가 없다는 것이다
# 왜냐하면, a[i][j]는 모두 0보다 크거나 같으며
# 최댓값을 구하는 과정이기 때문에
# 사실, 대각선으로 가는 것보다는
# 오른쪽 + 아래 // 아래 + 오른쪽 --> 대각선으로 가는 과정보다 더 크거나 같기 때문이다
# ( 중요 ) a[i][j]가 0보다 크거나 같다는 조건이 있기 때문에 가능한 것이다
n, m = map(int, input().split())
a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i-1][j], d[i][j-1])+a[i][j]
print(d[n][m])

'''
#include <cstdio>
#include <algorithm>
using namespace std;
int a[1001][1001];
int d[1001][1001];
int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            scanf("%d",&a[i][j]);
        }
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            d[i][j] = max(d[i-1][j],d[i][j-1])+a[i][j];
        }
    }
    printf("%d\n",d[n][m]);
    return 0;
}
'''

# 5) Top-Down
# 5_1) 시간초과
# 첫번째 문제 풀이 : 시간 초과 ( Top- Down approach ) ----

'''
d[i][j]
== i,j 번째 idx 까지 왔을 때, 먹을 수 있는
사탕의 최댓값 
'''

n, m = map(int, input().split())
# n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]


def dfs(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    if x == 0 and y == 0:
        return a[x][y]
    else:
        if y == 0:
            dp[x][y] = dfs(x-1, y) + a[x][y]
        elif x == 0:
            dp[x][y] = dfs(x, y-1) + a[x][y]
        else:
            dp[x][y] = ma
            x(dfs(x-1, y), dfs(x, y-1), dfs(x-1, y-1)) + a[x][y]
        return dp[x][y]


print(dfs(n-1, m-1))
# go(i,j) : d[i][j]를 구하는 것

# 5_2) 백준 풀이 : 방법 1을 top - down 으로 바꾸기
# 두번째 문제 풀이 : 시간 초과 ( Top- Down approach ) ----
n, m = map(int, input().split())
a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
'''
< 주의할 점 > ---

초기화를 무조건 -1로 해주어야 한다
또한 아래에서 memoization에서 if d[i][j] >= 0: 와 같이
반드시 >= ! 0보다 크거나 같다 ! 를 해주어야 한다

< 왜 그런것일까 ? > ---

d = [[0]*(m+1) for _ in range(n+1)] 와 같이, 초기화를 0으로 해주고 
if d[i][j] > 0: 라는 조건으로 memoization을 해주었다고 해보자
a[i][j] 는 무조건 0보다 크거나 같은 형태를 띤다 

그런데 우리는 memoization의 조건을 , 
즉 더이상 dfs 진행하지 말고, 저장된 값을 바로 리턴해라 !! 라는 조건을
if d[i][j] > 0: 로 해주고 있었다

만일 아래와 같이, 모든 원소가 0이라는 값을 가지게 된다면
0 0 0
0 0 0
0 0 0 

이 경우에 대해서는 memoization이 전혀 작동하지 않는다.

따라서, memoization을 바꿔주는 과정이 반드시 필요한데, 
이를 위해, 모든 d를 -1로 세팅해둔다

d[i][j]가 -1 이라는 것은, 해당 좌표에 대해서 아직 d[i][j]값을 구하지 
않은 것을 의미한다
왜냐하면 d[i][j] = max(go(i-1, j), go(i, j-1))+a[i][j] 이고, 
a[i][j] 는 무조건 0보다 크거나 같은 상황에서
d[i][j]를 구했다면, 최소 0이상의 값이 저장되어 있어야 하기 때문이다 

'''
d = [[-1]*(m+1) for _ in range(n+1)]


def go(i, j):
    # bottom up과 달리, 범위를 정해주는 과정
    if i < 1 or j < 1:  # i,j 가 1보다 작으면, 불가능한 경우 --> 0을 return
        return 0
    if d[i][j] >= 0:  # memoization --> top-down 과정에서 가장 중요한 것
        return d[i][j]
    d[i][j] = max(go(i-1, j), go(i, j-1))+a[i][j]
    return d[i][j]


print(go(n, m))

# 6) Top-Down -----------------------------------------------
# d[i][j]가 '시작점'에서 (i,j)로 가는 것을 의미했다면
# 여기서는 (i,j) 에서 '도착점'까지 가는 것으로 정의하려고 한다
# 그 말은 즉슨 (1,1)로 갈수록, 더 큰 문제에 해당하게 되는 것이다
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
a = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
d = [[-1]*(m+1) for _ in range(n+1)]


def go(i, j):
    if i > n or j > m:
        return 0
    if d[i][j] >= 0:
        return d[i][j]
    d[i][j] = max(go(i+1, j), go(i, j+1))+a[i][j]
    return d[i][j]


print(go(1, 1))

'''
#include <cstdio>
#include <algorithm>
using namespace std;
int a[1001][1001];
int d[1001][1001];
int n,m;
int go(int i, int j) {
    if (i > n || j > m) {
        return 0;
    }
    if (d[i][j] >= 0) {
        return d[i][j];
    }
    d[i][j] = max(go(i+1,j), go(i,j+1)) + a[i][j];
    return d[i][j];
}
int main() {
    scanf("%d %d",&n,&m);
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            scanf("%d",&a[i][j]);
            d[i][j] = -1;
        }
    }
    printf("%d\n",go(1,1));
    return 0;
}
'''
