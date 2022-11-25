# https://www.acmicpc.net/problem/17143

# 첫번째 풀이 : 성공 !
import sys
import heapq
import math
import copy
from collections import deque
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]  # 위,아래,오,왼
dy = [0, 0, 1, -1]  # 1,2,3,4

'''
1) C+1 만큼 반복
- 먼저, 해당 열에서, 가장 작은 행의 상어를 잡는다 
2) 모든 배열을 돌면서, 이동시켜야할 곳으로 이동(R*C)
3) 이동시킨 정보를 기존 배열에 update
4) 만약 다수의 상어가 존재한다면,
상어끼리의 먹음을 처리한다
5) 위의 과정을 반복한다 
'''

R, C, M = map(int, input().split())
maps = [[[] for _ in range(C)] for _ in range(R)]
sharks = []


def moveSk(r, c, tmps):
    spd, dirc, size = maps[r][c][0]
    nr, nc = r, c
    for _ in range(spd):
        nr, nc = nr + dx[dirc], nc + dy[dirc]
        if 0 > nr or R <= nr or 0 > nc or C <= nc:
            nr -= dx[dirc]
            nc -= dy[dirc]
            if dirc == 0:
                dirc = 1
            elif dirc == 1:
                dirc = 0
            elif dirc == 2:
                dirc = 3
            elif dirc == 3:
                dirc = 2
            nr += dx[dirc]
            nc += dy[dirc]
    tmps[nr][nc].append((spd, dirc, size))


for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    maps[r-1][c-1].append((s, d-1, z))

for ps in range(C):
    # 해당 열에서 가장 가까운 상어 잡기
    for row in range(R):
        if len(maps[row][ps]) > 0:
            sharks.append(maps[row][ps][0])
            maps[row][ps] = []
            break
    tmps = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if len(maps[i][j]) > 0:
                moveSk(i, j, tmps)
    # 상어끼리 잡아먹기 처리
    for i in range(R):
        for j in range(C):
            # 1마리
            if len(tmps[i][j]) == 1:
                maps[i][j] = [tmps[i][j][0]]
            # 2마리 이상
            elif len(tmps[i][j]) > 1:
                maxV = 0
                maxS = ''
                for t in tmps[i][j]:
                    s, d, z = t
                    if z > maxV:
                        maxV = z
                        maxS = (s, d, z)
                s, d, z = maxS
                maps[i][j] = [(s, d, z)]
            # 없으면
            else:
                maps[i][j] = []
ans = 0
for shark in sharks:
    s, d, z = shark
    ans += z
print(ans)


# 2번째  ------------------------------------------
# 시간 초과 :
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def changeDir(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2


R, C, M = map(int, input().split())
maps = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    maps[r-1][c-1].append((s, d-1, z))

res = 0
for c in range(C):
    for r in range(R):
        if len(maps[r][c]) > 0:
            res += maps[r][c][0][2]
            maps[r][c] = []
            break
    maps_c = [[[] for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if len(maps[x][y]) > 0:
                cur_sp, cur_d, cur_sz = maps[x][y][0]
                cx, cy = x, y
                for _ in range(cur_sp):
                    nx, ny = cx+dx[cur_d], cy+dy[cur_d]
                    if 0 > nx or R <= nx or 0 > ny or C <= ny:
                        cur_d = changeDir(cur_d)
                        nx, ny = cx+dx[cur_d], cy+dy[cur_d]
                    cx, cy = nx, ny
                if len(maps_c[cx][cy]) == 0:
                    maps_c[cx][cy].append((cur_sp, cur_d, cur_sz))
                else:
                    if maps_c[cx][cy][0][2] < cur_sz:
                        maps_c[cx][cy] = []
                        maps_c[cx][cy].append((cur_sp, cur_d, cur_sz))
    maps = maps_c
print(res)


# 3번째 ---
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def changeDir(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2
    return -1


R, C, M = map(int, input().split())
size = [[0]*C for _ in range(R)]
direction = [[0]*C for _ in range(R)]
speed = [[0]*C for _ in range(R)]

# 사람 이동
# 1) 사람이 오른쪽으로 한칸 이동
# 2) 땅과 가장 가까운 상어 잡기( 제일 행이 낮은 것 )
# 3) 상어 잡으면, 격자판에서 상어 사라짐 --> maps에서 사라짐

# 상어 이동
# 1) 주어진 속도로 이동
# 2) 이동하려는 칸이 경계넘으면, 반대로 이동
# 3) 2마리 이상 ? 크기가 가장 큰 상어가 나머지 모두 잡아먹는다.

for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    size[r-1][c-1] = z
    direction[r-1][c-1] = d-1
    speed[r-1][c-1] = s

res = 0

# 사람 이동
for c in range(C):
    # 상어 잡기
    for r in range(R):
        if size[r][c] != 0:
            res += size[r][c]
            size[r][c] = 0
            direction[r][c] = -1
            speed[r][c] = 0
            break
    # 상어 이동
    size_c = [[0]*C for _ in range(R)]
    direction_c = [[0]*C for _ in range(R)]
    speed_c = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if size[x][y] != 0:
                # 이동 처리
                cur_sz = size[x][y]
                cur_s = speed[x][y]
                cur_d = direction[x][y]
                cx, cy = x, y
                for s in range(cur_s):
                    nx, ny = cx+dx[cur_d], cy+dy[cur_d]
                    if 0 > nx or R <= nx or 0 > ny or C <= ny:
                        cur_d = changeDir(cur_d)
                        nx, ny = cx+dx[cur_d], cy+dy[cur_d]
                    cx, cy = nx, ny
                if size_c[cx][cy] < cur_sz:
                    size_c[cx][cy] = cur_sz
                    direction_c[cx][cy] = cur_d
                    speed_c[cx][cy] = cur_s
    # 이동 완료후, 배열 복사
    size = size_c
    direction = direction_c
    speed = speed_c
print(res)


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


'''
1. 상어가 이동할때 속도 크기만큼 한칸씩 이동하는게 아니라, 나머지 연산을 이용해서 한번에 이동하는 방법을 사용해볼 필요가 있을거같고,
2. 모든 좌표에 대해서 상어를 탐색하지 말고, 각 상어를 따로 테이블에 저장하고, 바로바로 상어를 탐색할 수 있게 개선하는게 맞다고 봅니다

maps_c를 생성하지 않고, 기존 맵에서 처리하는 방법을 생각해보시면
새로 할당하는 시간과 공간도 아낄 수 있을겁니다


예를들어 상어마다 번호를 매기고\작은 idx의 상어부터 움직였을때
작은idx가 큰 idx를 만났을때는 무시하고
큰 idx가 작은 idx 만났을때만 잡아먹는 로직을
실행시키는 방법도 있죠

아니면 2번째 코드처럼
먼저 이동 다 시키고 나서

상어 잡아먹는 연산을 실행하는 방법도 있다.
또한 모든 상어 정보를 맵에 저장할 필요없이
상어 정보는 리스트 형태로 저장해두고
맵에는 상어 인덱스칸 
저장하는 식으로 해도 좋다 

'''
