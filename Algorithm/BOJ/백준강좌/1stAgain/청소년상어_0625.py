#

from copy import deepcopy

n = 4
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#


def go(num, direction, x, y, d):
    for who in range(1, n*n+1):
        f = False
        for i in range(n):
            for j in range(n):
                if num[i][j] == who:
                    for k in range(8):
                        nx = i+dx[direction[i][j]]
                        ny = j+dy[direction[i][j]]
                        if 0 <= nx < n and 0 <= ny < n and num[nx][ny] >= 0 and (not (nx == x and ny == y)):
                            num[i][j], num[nx][ny] = num[nx][ny], num[i][j]
                            direction[i][j], direction[nx][ny] = direction[nx][ny], direction[i][j]
                            f = True
                            break
                        else:
                            direction[i][j] += 1
                            direction[i][j] %= 8
                if f:
                    break
            if f:
                break
    ans = 0
    sx = x+dx[d]
    sy = y+dy[d]
    while 0 <= sx < n and 0 <= sy < n:
        if num[sx][sy] != 0:
            temp = num[sx][sy]
            num[sx][sy] = 0
            # deepcopy를 해주는 이유는
            # 값복사를 해주기 위함이다
            cur = temp + go(deepcopy(num), deepcopy(direction),
                            sx, sy, direction[sx][sy])
            if ans < cur:
                ans = cur
            num[sx][sy] = temp
        sx += dx[d]
        sy += dy[d]

    return ans


num = [[0]*n for _ in range(n)]
direction = [[0]*n for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        num[i][j] = temp[2*j]
        direction[i][j] = temp[2*j+1]
        direction[i][j] -= 1
ans = num[0][0]
num[0][0] = 0
ans += go(num, direction, 0, 0, direction[0][0])
print(ans)

'''
C++

#include <iostream>
#include <vector>
using namespace std;
const int n = 4;
int dx[] = {-1,-1,0,1,1,1,0,-1};
int dy[] = {0,-1,-1,-1,0,1,1,1};

// num,dir : 물고기 번호 및 방향 
// x,y : 상어 위치
// d   : 상어 이동 방향 
int go(vector<vector<int>> num, vector<vector<int>> dir, int x, int y, int d) {
    // 누가 이동해야 하는지 찾아준다 
    // who를 왜 하는 건데 ?
    // 왜냐하면 번호가 작은 물고기부터 순서대로
    // 이동한다고 했기 때문이다 
    for (int who=1; who<=n*n; who++) {
        bool f = false;
        // who 라는 애를 찾아준다
        // (i,j)에 who 라는 물고기가 있는 것이다  
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (num[i][j] == who) {
                    for (int k=0; k<8; k++) {
                        // 최대 8번 회전하면서
                        // 어디로 이동할지 조사 
                        int nx = i+dx[dir[i][j]];
                        int ny = j+dy[dir[i][j]];
                        
                        // 경계안에 있고
                        // 물고기가 존재 혹은 빈칸
                        // 상어의 위치와 다르면 
                        if (0 <= nx && nx < n && 0 <= ny && ny < n && num[nx][ny] >= 0 && !(nx == x && ny == y)) {
                            swap(num[i][j], num[nx][ny]);
                            swap(dir[i][j], dir[nx][ny]);
                            // 물고기 이동 표시 
                            f = true;
                            break;
                        } else {
                            // 45도 회전
                            dir[i][j] += 1;
                            dir[i][j] %= 8;
                        }
                    }
                }
                if (f) break;
            }
            if (f) break;
        }
    }

    // 이제 상어 이동 처리 
    int ans = 0;
    int sx = x+dx[d];
    int sy = y+dy[d];
    // 상어 이동할 수 있다면
    // 1) 범위 안
    // 2) 해당 칸에 물고기가 있어야 함 
    while (0 <= sx && sx < n && 0 <= sy && sy < n) {
        // 물고기가 있다면 
        // 아래의 조건을 while 과 함께 넣으면 안된다
        // 상어->물->빈->물
        // 그런데 중간에 빈칸이 있다고 종료해버리면
        // 해당 방향으로 먹을 수 있는 모든 물고기를
        // 고려하지 못하게 되는 것이다 
        if (num[sx][sy] != 0) {
            int temp = num[sx][sy];
            num[sx][sy] = 0;
            // 해당 방향으로 상어 이동 
            int cur = temp + go(num, dir, sx, sy, dir[sx][sy]);
            if (ans < cur) ans = cur;
            // 이동이 끝나고 나면, 
            // 해당 위치에서 물고기를 먹은 경우를
            // 모두 고려한 것이므로, 
            // 다시 원래 상태로 되돌려준다 
            num[sx][sy] = temp;
        }
        // 해당 방향으로, 상어를 또 한칸 이동시킨다 
        sx += dx[d];
        sy += dy[d];
    }
    return ans;
}
int main() {
    // 물고기 번호 
    vector<vector<int>> num(n, vector<int>(n));
    // 물고기 방향 
    vector<vector<int>> dir(n, vector<int>(n));
    // 입력값 세팅 
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            // 입력 받고 
            cin >> num[i][j] >> dir[i][j];
            // 방향을 빼준다 
            dir[i][j] -= 1;
        }
    }

    // (0,0) 에서 시작하기 
    int ans = num[0][0];
    // 상어는 '0' 이라고 하려고 한다 
    num[0][0] = 0;
    // 이동 처리 
    ans += go(num, dir, 0, 0, dir[0][0]);
    cout << ans << '\n';
    return 0;
}

'''
