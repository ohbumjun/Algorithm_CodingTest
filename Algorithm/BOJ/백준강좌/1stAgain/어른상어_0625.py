# https://www.acmicpc.net/problem/19237

'''
----- <필요한 정보> -----
--> 상어를 저장하기 
(번호,위치,방향)
shark[i][j] : 어떤 상어가 들어있는지
기록해야 한다

--> dirs[k]
k번 상어 방향 

--> smell[i][j]
(i,j)에 있는 냄새가
사라지기 까지 필요한 시간

(문제 : 자신의 냄새)
smell_who[i][j]
누구의 냄새인지도 알아야 한다 
즉, smell_who[i][j] : 누구껀지

'''
import sys
limit = 1000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, smell_time = map(int, input().split())
shark = [[0]*n for _ in range(n)]
shark_next = [[0]*n for _ in range(n)]
smell = [[0]*n for _ in range(n)]
smell_who = [[0]*n for _ in range(n)]
dirs = [0] * (m+1)
priority = [[[0]*4 for _ in range(4)] for __ in range(m+1)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        shark[i][j] = temp[j]
        if shark[i][j] > 0:
            smell[i][j] = smell_time
            smell_who[i][j] = shark[i][j]

dirs = [0] + [d-1 for d in map(int, input().split())]

for i in range(1, m+1):
    for j in range(4):
        priority[i][j] = [d-1 for d in map(int, input().split())]


def check_1():
    cnt = 0
    one = 0
    for i in range(n):
        for j in range(n):
            if shark[i][j] > 0:
                cnt += 1
            if shark[i][j] == 1:
                one += 1
    return cnt == 1


def move_shark():
    v = []
    for i in range(n):
        for j in range(n):
            shark_next[i][j] = 0
            if shark[i][j] > 0:
                v.append((shark[i][j], i, j))
    v.sort()

    for t in v:
        no, x, y = t
        shark_dir = dirs[no]
        ok = False

        for k in range(4):
            nx = x+dx[priority[no][shark_dir][k]]
            ny = y+dy[priority[no][shark_dir][k]]
            if 0 <= nx < n and 0 <= ny < n:
                if smell[nx][ny] == 0:
                    if shark_next[nx][ny] == 0:
                        shark_next[nx][ny] = no
                        dirs[no] = priority[no][shark_dir][k]
                    else:
                        if shark_next[nx][ny] > no:
                            shark_next[nx][ny] = no
                            dirs[no] = priority[no][shark_dir][k]

                    ok = True
                    break
            if ok:
                break
        if not ok:
            for k in range(4):
                nx = x+dx[priority[no][shark_dir][k]]
                ny = y+dy[priority[no][shark_dir][k]]
                if 0 <= nx < n and 0 <= ny < n:
                    if smell[nx][ny] > 0 and smell_who[nx][ny] == no:
                        shark_next[nx][ny] = no
                        dirs[no] = priority[no][shark_dir][k]
                        ok = True
                        break
                if ok:
                    break

    for i in range(n):
        for j in range(n):
            shark[i][j] = shark_next[i][j]
            if smell[i][j] > 0:
                smell[i][j] -= 1
            if smell[i][j] == 0:
                smell_who[i][j] = 0
            if shark[i][j] > 0:
                smell[i][j] = smell_time
                smell_who[i][j] = shark[i][j]


ans = -1

for t in range(1, limit+1):
    move_shark()
    if check_1():
        ans = t
        break
print(ans)


'''
C++ -----

#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
using namespace std;
const int limit = 1000;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
int shark[20][20];      // 현재 위치 상어
int shark_next[20][20]; // 다음 위치 상어 --> 이후 shark 배열 덮어씌울 것
int smell[20][20];
int smell_who[20][20];
int dir[401];

// priority[i][j] : i번 상어의 방향이 j일 때 
int priority[401][4][4];

// 크기, 상어의 수, 냄새 지속 시간 
int n, m, smell_time;

// 1번 상어 1마리만 남으면 된다 
bool check_1() {
    int cnt = 0;
    int one = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            // 상어가 잇으면 개수 세어주기 
            if (shark[i][j] > 0) {
                cnt += 1;
            }
        }
    }
    return cnt == 1;
}


void move_shark() {
    // 상어의 번호, 행, 열 
    vector<tuple<int,int,int>> v; // no, x, y
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            // 맨처음에는 다음 상어를 모두 0으로 초기화 
            shark_next[i][j] = 0;
            // 상어가 있으면, 상어 정보 넣어주기 
            if (shark[i][j] > 0) {
                v.push_back(make_tuple(shark[i][j], i, j));
            }
        }
    }
    // 번호가 작은 상어부터 이동 처리  
    sort(v.begin(), v.end());

    for (auto &t : v) {
        // no  : 현재 상어의 번호 
        // x,y : 상어의 행과 열 
        int no, x, y;
        tie(no, x, y) = t;
        // shark_dir : 상어의 방향 
        int shark_dir = dir[no];
        bool ok = false;
        // 4개 방향 인접한 곳에서
        // 갈 수 있는 곳을 살핀다 
        // 즉, 냄새가 없는 곳을 살핀다 
        for (int k=0; k<4; k++) {
            int nx = x+dx[priority[no][shark_dir][k]];
            int ny = y+dy[priority[no][shark_dir][k]];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                // 인접한 4개의 칸 중에서
                // 냄새가 없는 칸 조사하기 
                if (smell[nx][ny] == 0) {
                    // 상어도 없다면 
                    if (shark_next[nx][ny] == 0) {
                        // 해당 위치로 이동해주기 
                        shark_next[nx][ny] = no;
                        dir[no] = priority[no][shark_dir][k];
                    } else {
                        // 그게 아니라면
                        // 상어가 있다면
                        // 현재 움직이려는 상어의 
                        // 번호가 더 작을 때만 
                        // 왜냐하면, 번호가 더 작은 상어가
                        // 우선적으로 해당 영역을 차지하기 때문이다
                        if (shark_next[nx][ny] > no) {
                            shark_next[nx][ny] = no;
                            dir[no] = priority[no][shark_dir][k];
                        }
                    }
                    ok = true;
                    break;
                }
            }
            if (ok) break;
        }

        // 만약 그러한 칸이 없다
        // 냄새가 없는 칸이 없다
        // 이 경우, 자신의 냄새가 있는 칸의 방향으로 잡는다 
        // 그러면, 조사를 시작해야 한다 
        // 방향 우선 순위대로 움직여야 한다 
        if (!ok) {
            for (int k=0; k<4; k++) {
                // priority[no] : 상어마다
                // priority[no][shark_dir] : 해당 상어가 바라보고 있는 방향마다
                // priority[no][shark_dir][k] : 4방향의 우선순위가 모두 다르다 
                int nx = x+dx[priority[no][shark_dir][k]];
                int ny = y+dy[priority[no][shark_dir][k]];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    // 자신이 있는 칸을 조사하기 
                    // smell[nx][ny] : 해당 영역에 냄새가 존재 
                    if (smell[nx][ny] > 0 && smell_who[nx][ny] == no) {
                        shark_next[nx][ny] = no;
                        dir[no] = priority[no][shark_dir][k];
                        ok = true;
                        break;
                    }
                }
                if (ok) break;
            }
        }
    }
    // 이제 상어를 이동키시자 
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            shark[i][j] = shark_next[i][j];
            // 냄새 1 깍고 
            if (smell[i][j] > 0) {
                smell[i][j] -= 1;
            }
            // 냄새없어지면, 해당 냄새 주인도 없애주기 
            if (smell[i][j] == 0) {
                smell_who[i][j] = 0;
            }
            // 새로운 상어 정보 setting
            if (shark[i][j] > 0) {
                smell[i][j] = smell_time;
                smell_who[i][j] = shark[i][j];
            }
        }
    }
}
int main() {
    cin >> n >> m >> smell_time;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> shark[i][j];
            if (shark[i][j] > 0) {
                smell[i][j] = smell_time;
                smell_who[i][j] = shark[i][j];
            }
        }
    }
    for (int i=1; i<=m; i++) {
        cin >> dir[i];
        dir[i] -= 1;
    }
    for (int i=1; i<=m; i++) {
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                cin >> priority[i][j][k];
                priority[i][j][k] -= 1;
            }
        }
    }
    int ans = -1;
    for (int t=1; t<=limit; t++) {
        move_shark();
        if (check_1()) {
            ans = t;
            break;
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
