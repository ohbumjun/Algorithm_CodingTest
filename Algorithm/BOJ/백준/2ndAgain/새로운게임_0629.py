# https://www.acmicpc.net/problem/17780

'''
<정보>
1) 체스판에 대한 정보
board[i][j] = (i,j) 색

2) 말에 대한 정보
- 말 하나를 표현하는 정보
- 번호, 위치, 방향 
- <2가지 방법이 존재한다>
- => a[i][j] = (i,j)에 있는 말을 저장 : 어떤 위치에 어떤 말이 있는지 알기 쉽다
 => 단, 특정 말이 어디에 있는지는 알기 어렵다
- => where[k] = i번 말의 위치  : 특정 말이 어디에 있는지 알기 쉽고 
=> 단, 어떤 위치에 어떤 말이 있는지는 알기 어렵다 

둘다 이용해야 한다
=> 말을 이동할때에는, 어디에 어떤 말이 있는지 알아야
말을 쌓거나 할 수 있고
=> 1번부터 k번까지의 말을 이동시키기 위해서, 
어떤 말이 어디에 있는지도 알아야 한다 

-------------------------------------------------------
흰,빨,파란색 경우에 대해서 일괄되게 처리하기 위하여, 
1) 파란색인 경우에,
방향만 바꾸는 것을 먼저 처리한 이후,
2) 빨간색인 경우는, 그냥 먼저 뒤집고
(즉, 뒤집고 이동하나, 이동하고 뒤집나 같은 원리 )

같은 이동원리를
흰,빨,파에 모두 적용하면 된다.

'''
import sys


class Piece:
    def __init__(self, no, direction):
        self.no = no
        self.direction = direction


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def opposite(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    return 2


def go(a, where, x, y, nx, ny):
    for p in a[x][y]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny)
    a[x][y].clear()


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m

for i in range(m):
    x, y, direction = map(int, input().split())
    a[x-1][y-1].append(Piece(i, direction-1))
    where[i] = (x-1, y-1)

for turn in range(1, 1001):
    for k in range(m):
        x, y = where[k]
        if a[x][y][0].no == k:  # bottom
            direction = a[x][y][0].direction
            nx = x+dx[direction]
            ny = y+dy[direction]
            if 0 <= nx < n and 0 <= ny < n:  # in
                if board[nx][ny] == 2:
                    a[x][y][0].direction = opposite(direction)
            else:
                a[x][y][0].direction = opposite(direction)
            direction = a[x][y][0].direction
            nx = x+dx[direction]
            ny = y+dy[direction]

            if 0 <= nx < n and 0 <= ny < n:  # in
                if board[nx][ny] == 0:
                    go(a, where, x, y, nx, ny)
                elif board[nx][ny] == 1:
                    a[x][y].reverse()
                    go(a, where, x, y, nx, ny)
                if len(a[nx][ny]) >= 4:
                    print(turn)
                    sys.exit(0)
            else:  # out
                pass
print(-1)

'''
#include <iostream>
#include <tuple>
#include <algorithm>
#include <vector>
using namespace std;
int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};
int opposite(int dir) {
    if (dir == 0) return 1;
    if (dir == 1) return 0;
    if (dir == 2) return 3;
    return 2;
}
void go(vector<vector<vector<pair<int,int>>>> &a, vector<pair<int,int>> &where, int x, int y, int nx, int ny) {
    for (auto &p : a[x][y]) {
        // 새로운 위치로 이동 x,y --> nx,ny
        a[nx][ny].push_back(p);
        // where 정보도 update 
        where[p.first] = make_pair(nx, ny);
    }
    // 이동 후에 비워주기 
    a[x][y].clear();
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> board[i][j];
        }
    }
    vector<vector<vector<pair<int,int>>>> a(n, vector<vector<pair<int,int>>>(n));
    vector<pair<int,int>> where(m);
    // 입력 받고 말의 정보 저장 
    for (int i=0; i<m; i++) {
        int x, y, dir;
        cin >> x >> y >> dir;
        a[x-1][y-1].push_back(make_pair(i, dir-1));
        where[i] = make_pair(x-1, y-1);
    }
    // 최대1000번까지 가능
    for (int turn=1; turn<=1000; turn++) {
        for (int k=0; k<m; k++) {
            int x, y;

            // 어떤 말이 어디에 있는지 알아내기 위해
            // where를 활용한다 
            tie(x,y) = where[k];

            // k번말의 위치 상에서 [0]번째
            // 즉, 맨 아래에 있다면, 해당 k 말의 정보를
            // 기준으로 이동처리를 해준다 
            if (a[x][y][0].first == k) { // bottom
                int dir = a[x][y][0].second;
                int nx = x+dx[dir];
                int ny = y+dy[dir];

                // 범위 안이면
                if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                    // 파란색이라면 
                    if (board[nx][ny] == 2) {
                        a[x][y][0].second = opposite(dir);
                        // 원래 파랑색이라면, 방향 바꿔주고, 이동까지 해야 한다
                        // 그런데 여기서는 방향만 바꿔주고
                        // 실제 이동은 아래에서 함께 처리한다 
                    }
                    // 범위 밖이라면 
                } else {
                    a[x][y][0].second = opposite(dir);
                }

                // 변경된 방향을 다시 저장
                dir = a[x][y][0].second;
                nx = x+dx[dir];
                ny = y+dy[dir];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                    // 흰색인 경우에는 그냥 이동
                    if (board[nx][ny] == 0) {
                        go(a, where, x, y, nx, ny);
                    } else if (board[nx][ny] == 1) {
                        // 빨간색 칸이면 일단 뒤집고
                        reverse(a[x][y].begin(), a[x][y].end());
                        // 이동시키고
                        go(a, where, x, y, nx, ny);
                    }
                    if (a[nx][ny].size() >= 4) {
                        cout << turn << '\n';
                        return 0;
                    }
                } else { // out
                }
            }
        }
    }
    cout << -1 << '\n';
    return 0;
}

'''
