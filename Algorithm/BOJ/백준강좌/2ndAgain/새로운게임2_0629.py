# 가장 아래에 있는 요소만 움직인다. 라는 조건이 빠진다
# https://www.acmicpc.net/problem/17837

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


'''
def go(a, where, x, y, nx, ny):
    for p in a[x][y]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny)
    a[x][y].clear()

    가장 아래에 있는 애만 움직인다
    따라서, 모두가 같은 방향으로 움직이는 코드 
'''


def go(a, where, x, y, nx, ny, start):
    # start 번째부터 이동할 수 있게 해주었다
    # 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다
    # 즉, start 지점 그 위의 말들을 모두 이동시켜주는 것이다
    for i in range(start, len(a[x][y])):
        p = a[x][y][i]
        a[nx][ny].append(p)
        # len(a[nx][ny])-1 : 위치(해당 행,열에서 몇번째)
        where[p.no] = (nx, ny, len(a[nx][ny])-1)
    a[x][y] = a[x][y][:start]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m

for i in range(m):
    x, y, direction = map(int, input().split())
    a[x-1][y-1].append(Piece(i, direction-1))
    # 새로운 게임1 에서는 (행,열)위치만 중요했다
    # 하지만, 이제는 해당 위치에서 , 몇번째에 쌓여있는지도 알아야 한다
    where[i] = (x-1, y-1, len(a[x-1][y-1])-1)

for turn in range(1, 1001):
    for k in range(m):
        x, y, index = where[k]
        direction = a[x][y][index].direction
        nx = x+dx[direction]
        ny = y+dy[direction]
        if 0 <= nx < n and 0 <= ny < n:  # in
            if board[nx][ny] == 2:
                a[x][y][index].direction = opposite(direction)
        else:
            a[x][y][index].direction = opposite(direction)
        direction = a[x][y][index].direction
        # updata 한 방향에 근거한, 새로운 위치
        nx = x+dx[direction]
        ny = y+dy[direction]

        if 0 <= nx < n and 0 <= ny < n:  # in
            if board[nx][ny] == 0:
                go(a, where, x, y, nx, ny, index)
            elif board[nx][ny] == 1:
                a[x][y] = a[x][y][:index] + a[x][y][index:][::-1]
                go(a, where, x, y, nx, ny, index)
            if len(a[nx][ny]) >= 4:
                print(turn)
                sys.exit(0)
        else:  # out
            pass
print(-1)

'''
C++

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
void go(vector<vector<vector<pair<int,int>>>> &a, vector<tuple<int,int,int>> &where, int x, int y, int nx, int ny, int start) {
    for (int i=start; i<a[x][y].size(); i++) {
        auto &p = a[x][y][i];
        a[nx][ny].push_back(p);
        where[p.first] = make_tuple(nx, ny, (int)a[nx][ny].size()-1);
    }
    a[x][y].resize(start);
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
    vector<tuple<int,int,int>> where(m);
    for (int i=0; i<m; i++) {
        int x, y, dir;
        cin >> x >> y >> dir;
        a[x-1][y-1].push_back(make_pair(i, dir-1));
        where[i] = make_tuple(x-1, y-1, (int)a[x-1][y-1].size()-1);
    }
    for (int turn=1; turn<=1000; turn++) {
        for (int k=0; k<m; k++) {
            int x, y, index;
            tie(x,y,index) = where[k];
            int dir = a[x][y][index].second;
            int nx = x+dx[dir];
            int ny = y+dy[dir];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                if (board[nx][ny] == 2) {
                    a[x][y][index].second = opposite(dir);
                }
            } else {
                a[x][y][index].second = opposite(dir);
            }
            dir = a[x][y][index].second;
            nx = x+dx[dir];
            ny = y+dy[dir];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) { // in
                if (board[nx][ny] == 0) {
                    go(a, where, x, y, nx, ny, index);
                } else if (board[nx][ny] == 1) {
                    reverse(a[x][y].begin()+index, a[x][y].end());
                    go(a, where, x, y, nx, ny, index);
                }
                if (a[nx][ny].size() >= 4) {
                    cout << turn << '\n';
                    return 0;
                }
            } else { // out
            }
        }
    }
    cout << -1 << '\n';
    return 0;
}

'''
