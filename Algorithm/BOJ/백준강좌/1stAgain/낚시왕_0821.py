# https://www.acmicpc.net/problem/17143

# 첫번째 풀이 : 메모리 초과
from copy import deepcopy
import heapq as hq
import sys
from functools import reduce
from collections import deque, defaultdict
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1501*1501)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 배열
ans = 0
R, C, m = map(int, input().split())
speed = [0]*(m+1)  # 속력
dirs = [0]*(m+1)  # 이동 방향
shark = [[(-1, -1)]*C for _ in range(R)]  # (번째,크기)
shark_next = [[0]*C for _ in range(R)]
temp = [list(map(int, input().split())) for _ in range(m)]
for t in range(m):
    r, c, s, d, z = temp[t]
    # 상어 정보
    shark[r-1][c-1] = (t+1, z)
    dirs[t+1] = d-1
    speed[t+1] = s


def opp(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    return 2


def catch_shark(c):
    global ans
    for i in range(R):
        if shark[i][c] != (-1, -1):
            ans += shark[i][c][1]
            shark[i][c] = (-1, -1)
            break


def move_shark():
    # shark_next 초기화
    v = []
    for i in range(R):
        for j in range(C):
            # 번째, 크기
            shark_next[i][j] = (-1, -1)
            if shark[i][j][0] > 0:
                idx, size = shark[i][j]
                # 크기,속력,방향
                v.append((idx, size, i, j))
    for e in v:
        idx, size, x, y = e
        sp, direc = speed[idx], dirs[idx]
        # 이동 처리
        fx, fy = x, y
        for i in range(sp):
            nx, ny = fx+dx[direc], fy+dy[direc]
            if 0 <= nx < R and 0 <= ny < C:
                fx, fy = nx, ny
            else:
                # 방향 전환
                direc = opp(direc)
                dirs[idx] = direc
                fx, fy = fx+dx[direc], fy+dy[direc]
        # fx,fy에 최종 이동 위치 세팅
        if shark_next[fx][fy] == (-1, -1):
            shark_next[fx][fy] = (idx, size)
        else:
            if shark_next[fx][fy][1] < size:
                shark_next[fx][fy] = (idx, size)
    # 이제 shark_next 정보 --> shark 복사하기
    for i in range(R):
        for j in range(C):
            shark[i][j] = shark_next[i][j]


for c in range(C):
    catch_shark(c)
    move_shark()
print(ans)


'''
<해설>
1) 상어에 대한 정보
--> 상어의 리스트
shark[i] = i번 상어의 정보

2) Shark[r][c]
--> (r,c) 에 있는 상어

"이동에서의 핵심은"
"동시에 이동" 이다 

2개의 배열
1) 이동 전
2) 이동 후 --> 이동 전 복사

---------------------------



'''


# Python

class Fish:
    def __init__(self, size=0, speed=0, direction=0):
        self.size = size
        self.speed = speed
        self.direction = direction


# up, down, right, left
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n, m, mm = map(int, input().split())
fish = [[Fish() for j in range(m)] for i in range(n)]
nfish = [[Fish() for j in range(m)] for i in range(n)]
for _ in range(mm):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    if d <= 1:
        s %= (2*n-2)
    else:
        s %= (2*m-2)
    fish[x][y] = Fish(z, s, d)


def get_next(x, y, speed, direction):
    for k in range(speed):
        if direction == 0:  # up
            if x == 0:
                x = 1
                direction = 1
            else:
                x -= 1
        elif direction == 1:  # down
            if x == n-1:
                x = n-2
                direction = 0
            else:
                x += 1
        elif direction == 2:  # right
            if y == m-1:
                y = m-2
                direction = 3
            else:
                y += 1
        elif direction == 3:  # left
            if y == 0:
                y = 1
                direction = 2
            else:
                y -= 1
    return (x, y, direction)


ans = 0
for j in range(m):
    for i in range(n):
        if fish[i][j].size > 0:
            ans += fish[i][j].size
            fish[i][j].size = 0
            break
    for l1 in range(n):
        for l2 in range(m):
            if fish[l1][l2].size == 0:
                continue
            f = fish[l1][l2]
            x, y, direction = get_next(l1, l2, f.speed, f.direction)
            if nfish[x][y].size == 0 or nfish[x][y].size < f.size:
                nfish[x][y] = Fish(f.size, f.speed, direction)
    for l1 in range(n
                    ):
        for l2 in range(m):
            fish[l1][l2] = Fish(nfish[l1][l2].size, nfish[l1]
                                [l2].speed, nfish[l1][l2].direction)
            nfish[l1][l2].size = 0

print(ans)


# C++
'''
#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
using namespace std;
struct Fish {
    int size = 0;      // 크기
    int speed = 0;     // 속도
    int direction = 0; // 방향 
};
// up, down, right, left
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};
int n, m;
Fish fish[100][100];
Fish nfish[100][100];
tuple<int,int,int> get_next(int x, int y, int speed, int direction) {
    for (int k=0; k<speed; k++) {
        if (direction == 0) { // up
            if (x == 0) {
                x = 1;
                direction = 1;
            } else {
                x -= 1;
            }
        } else if (direction == 1) { // down
            if (x == n-1) {
                x = n-2;
                direction = 0;
            } else {
                x += 1;
            }
        } else if (direction == 2) { // right
            if (y == m-1) {
                y = m-2;
                direction = 3;
            } else {
                y += 1;
            }
        } else if (direction == 3) { // left
            if (y == 0) {
                y = 1;
                direction = 2;
            } else {
                y -= 1;
            }
        }
    }
    return make_tuple(x, y, direction);
}
int main() {
    int mm;
    cin >> n >> m >> mm; // 행,열,mn : 상어의 수 
    while (mm--) {
        int x, y, s, d, z;
        // s : 속도 , z : 방향 
        cin >> x >> y >> s >> d >> z;
        x -= 1; // 행
        y -= 1; // 열
        d -= 1; // 방향 
        if (d <= 1) {
            s %= (2*n-2);
        } else {
            s %= (2*m-2);
        }
        fish[x][y] = Fish({z, s, d});
    }
    long long ans = 0;
    // 상어 잡음 
    for (int j=0; j<m; j++) {
        for (int i=0; i<n; i++) {
            if (fish[i][j].size > 0) {
                ans += fish[i][j].size;
                fish[i][j].size = 0;
                break;
            }
        }
        for (int l1=0; l1<n; l1++) {
            for (int l2=0; l2<m; l2++) {
                // 상어가 없는 경우 
                if (fish[l1][l2].size == 0) continue;
                auto f = fish[l1][l2];
                int x, y, direction;
                // 상어의 다음 위치, 방향, 속도 저장 
                tie(x, y, direction) = get_next(l1, l2, f.speed, f.direction);
                // nfish[x][y].size == 0 새로운 위치에 상어 없음
                // nfish[x][y].size < ~ : 현재 이동하는 애가 더 크다 
                if (nfish[x][y].size == 0 || nfish[x][y].size < f.size) {
                    nfish[x][y] = Fish({f.size, f.speed, direction});
                }
            }
        }
        for (int l1=0; l1<n; l1++) {
            for (int l2=0; l2<m; l2++) {
                fish[l1][l2] = nfish[l1][l2];
                nfish[l1][l2].size = 0;
            }
        }
    }
    cout << ans << '\n';
    return 0;
}

'''
