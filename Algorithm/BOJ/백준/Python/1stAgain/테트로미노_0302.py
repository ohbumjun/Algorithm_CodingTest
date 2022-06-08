# https://www.acmicpc.net/problem/14500

# 첫번째 풀이 : Brute Force
import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
ch = [[0] * m for _ in range(n)]
dCol = [-1, 0, 1, 0]
dRow = [0, -1, 0, 1]
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# x, y 좌표
# sum : 지금까지 간 간격에 있던 수들의 합 ----
# cnt : 몇칸 갔는지 ( 4칸까지 ! )


'''
노션 해설
https://www.notion.so/cdee042ce9b846198664fb80deb47fc1 //

x,y : 행 , 열
sum : 거기까지 칸에 써있는 수의 합 
cnt : 몇개의 칸을 방문했는가 

'''


def go(x, y, sum, cnt):
    global ans
    # 4개를 방문했다면, 얘는 테트로미노가 맞으니
    # 정답을 찾은 경우에 해당
    # ans ( 지금까지 구한 정답 )과의 최댓값 비교 수행
    if cnt == 4:
        if sum > ans:
            ans = sum

    # 이미 방문처리되었다면 or 범위를 벗어난다면
    if (x <= 0 or x >= n or y <= 0 or y >= m):
        return
    # 방문한 칸 또 방문했으면 return
    if (ch[x][y] == 1):
        return

    # 방문 처리 ( 다시해당 칸으로 돌아가지 않게 하기 위해서
    ch[x][y] = 1

    # 그렇지 않다면, 가능한 4개의 구간을 돈다
    for i in range(4):
        nx = x + dCol[i]
        ny = y + dRow[i]
        go(nx, ny, sum + arr[x][y], cnt + 1)

    # 방문 처리 풀어주기  ( 왜냐하면, 이후 다른 칸을 기준으로 진행될 때 여기도 방문시켜주어ㅑ 하기 때문이다 )
    # 참고 : dfs는 이부분이 절대 존재하지 않는다. 왜냐하면, dfs는 모든 정점을 '1번' 방문하는 것이 목적인데
    #       여기서 체크를 풀어버리면, 같은 정점을 1번보다 더 많이 방문하게 되기 때문이다
    ch[x][y] = 0


for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)

        if j + 2 < m:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            if i - 1 >= 0:
                tmp2 = tmp + arr[i][j+1]
                ans = max(ans, tmp2)
            if i + 1 < n:
                tmp2 = tmp + arr[i+1][j+1]
                ans = max(ans, tmp2)
        if i + 2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if j + 1 < m:
                tmp2 = tmp + arr[i+1][j+1]
                ans = max(tmp2, ans)
            if j - 1 >= 0:
                tmp2 = tmp + arr[i+1][j-1]
                ans = max(tmp2, ans)

print(ans)


'''
C++

#include <iostream>
using namespace std;
int a[500][500];
bool c[500][500];
int n, m;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int ans = 0;
void go(int x, int y, int sum, int cnt) {

    if (cnt == 4) {
        if (ans < sum) ans = sum;
        return;
    }
    if (x < 0 || x >= n || y < 0 || y >= m) return;
    if (c[x][y]) return;

    c[x][y] = true; 

    // [10][20][40][60]

    for (int k=0; k<4; k++) {
        go(x+dx[k],y+dy[k],sum+a[x][y],cnt+1);
    }

    c[x][y] = false;

}

int main() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            go(i,j,0,0);
            if (j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2];
                if (i-1 >= 0) {
                    int temp2 = temp + a[i-1][j+1];
                    if (ans < temp2) ans = temp2;
                }
                if (i+1 < n) {
                    int temp2 = temp + a[i+1][j+1];
                    if (ans < temp2) ans = temp2;
                }
            }
            if (i+2 < n) {
                int temp = a[i][j] + a[i+1][j] + a[i+2][j];
                if (j+1 < m) {
                    int temp2 = temp + a[i+1][j+1];
                    if (ans < temp2) ans = temp2;
                }
                if (j-1 >= 0) {
                    int temp2 = temp + a[i+1][j-1];
                    if (ans < temp2) ans = temp2;
                }
            }
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
