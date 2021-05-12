# https://www.acmicpc.net/problem/13460

from random import randrange, randint
import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''

구슬 이동 

방향 : 위, 아래, 왼쪽, 오른쪽 총 4개
횟수 : 최대 10번 

4 ^ 10

즉,
Brute Force : 1) 기울일 수 있는 모든 방향을 만들고 ( 재귀, 비트마스크 ) 
2) 문제 나와있는 대로 시뮬레이션 해보



< 모든 방향을 만들어보기 : 재귀 > -------------------------------
"기울여서" : 더 이상 구슬이 움직이지 않을 때까지 ??

이로 인해 우리는 방법의 개수를 4 ^ 10에서 조금 더 줄일 수 있다.
how ? 예를 들어, 왼쪽으로 쭉 물체를 이동시켰다면
물체들도 맨 왼쪽에 놓일 것이다.

여기서 물체들을 왼쪽으로 이동시켜도,
물체들은 이동하지 않을 것이다.

1) 같은 방향으로 이동시키는 것은 의미가 없다. 
즉, 이전에 이동시킨 방향으로는 이동시키지 않아도 되는 것이다.

맨 처음, 1번째 이동을 시킬 때에는
4가지 방향으로 모두 이동시킬 수 있다.

하지만, 2번째 이동 부터는 그 개수가 줄어든다.

2) 반대 방향으로의 이동도 의미가 없다.
처음에 왼쪽으로 이동시켰다가, 다시 오른쪽으로 이동시키기

사실 이건 그냥 처음에 오른쪽으로 이동시키는 것과 다름이 없다.

즉, 예를 들어, 1번째 이동에 왼쪽으로 이동시켰다면
2번째 이동에서는, 왼쪽 혹은 오른쪽.으로 이동시키는 것
둘다 의미가 없다는 것이다. ( 같은 방향, 반대 방향 )

그렇다면 왜 '의미가 없다'를 따지는 걸까?
왜냐하면 "최소 횟수"를 구하는 문제이기 때문이다.

즉, 1번째 이동때에는 4가지 이동 가짓수가 존재하지만,
2번째 이동부터는 2가지 이동 가짓수가 존재하는 것이다. 

결국 10번의 이동 가짓수를 따져보면
4 *  ( 2 ^ 9 ) = 2048 가지수.가 되는 것이다.

< 모든 방향을 만들어보기 : 비트마스크 > -------------------------

위, 오, 아, 왼
이라는 4개의 방향을 숫자로 표현할 수 있다
0   1   2    3

이것을 이어붙이면
위, 오, 아, 왼쪽으로 이동시켰다면
0 1 2 3
이라는 숫자를 만드는 것과 같고

이는 4진법의 표현이다.

4진법은, 2개의 2진법의 조합으로 표현할 수 있다.
왜 ?? 이진법에서는 2자리가, 0 ~ 3 이라는 숫자를 의미하기 때문이다.

그러므로, 
비트마스크로 2 ^ 20 을 만든 다음에,

해당 숫자를 2개씩 묶으면
그것이 바로 4진법의 수가 된다.

2개 묶을 때, 앞의 1은 2 , 뒤의 1은 1

ex) 다음과 같다

1 (0 1) (1 0) (1 1) (1 0)  ( 2개씩 묶게 된다면 )
1     1     2     3     2

해당 녀석을 코드로는 어떻게 구현할까?
맨 뒤 2자리씩 비교를 한다.
맨 뒤 2자리 & &3 을 하게 되면, 4진법으로 표현이 될 것이고
왼쪽으로 2번 더 이동해주기 위해서 << 2 를 실시하게 된다.

< 문제에 나와 있는 대로 시뮬레이션 하기 > ----------------------
1) 빨간 공, 파란 공 동시에 이동시키기.

동시에 이동시킨다는 조건이 매우 까다롭다.
사실 코드상으로 동시에 이동시킬 수 는 없기 때문에
우리가 순서를 정해주어야 한다.

빨간색을 먼저, 파란색을 2번째로 이동시킨다고 해보자.
그런데 이 경우에, 이동 횟수 및 방향에 제한이 생길 수 있다.

예를 들어, Red와 Blue 공이 있다고 해보자.
Red가 왼쪽, Blue가 오른쪽에 있고
오른쪽으로 기울이려고 하는데

Red가 Blue에 막혀, 온전히 오른쪽 옆으로 이동하지 못하는 경우가 생긴다는 것이다.
이 경우에는
1) Red를 Blue 전까지 오른쪽 이동
2) Blue 오른쪽 끝까지 이동
3) Red도 마저 오른쪽으로 이동시키기

즉, "기울임" 이라는 행위에는,
다음과 같은 요소들이 필요해진다.

빨 이동 + 파 이동 + 무한 반복 !
언제까지 ?
두 구슬의 위치가 변하지 않을때까지 !


'''

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''

구슬 이동 

방향 : 위, 아래, 왼쪽, 오른쪽 총 4개
횟수 : 최대 10번 

4 ^ 10

즉,
Brute Force : 1) 기울일 수 있는 모든 방향을 만들고 ( 재귀, 비트마스크 ) 
2) 문제 나와있는 대로 시뮬레이션 해보



< 모든 방향을 만들어보기 : 재귀 > -------------------------------
"기울여서" : 더 이상 구슬이 움직이지 않을 때까지 ??

이로 인해 우리는 방법의 개수를 4 ^ 10에서 조금 더 줄일 수 있다.
how ? 예를 들어, 왼쪽으로 쭉 물체를 이동시켰다면
물체들도 맨 왼쪽에 놓일 것이다.

여기서 물체들을 왼쪽으로 이동시켜도,
물체들은 이동하지 않을 것이다.

1) 같은 방향으로 이동시키는 것은 의미가 없다. 
즉, 이전에 이동시킨 방향으로는 이동시키지 않아도 되는 것이다.

맨 처음, 1번째 이동을 시킬 때에는
4가지 방향으로 모두 이동시킬 수 있다.

하지만, 2번째 이동 부터는 그 개수가 줄어든다.

2) 반대 방향으로의 이동도 의미가 없다.
처음에 왼쪽으로 이동시켰다가, 다시 오른쪽으로 이동시키기

사실 이건 그냥 처음에 오른쪽으로 이동시키는 것과 다름이 없다.

즉, 예를 들어, 1번째 이동에 왼쪽으로 이동시켰다면
2번째 이동에서는, 왼쪽 혹은 오른쪽.으로 이동시키는 것
둘다 의미가 없다는 것이다. ( 같은 방향, 반대 방향 )

그렇다면 왜 '의미가 없다'를 따지는 걸까?
왜냐하면 "최소 횟수"를 구하는 문제이기 때문이다.

즉, 1번째 이동때에는 4가지 이동 가짓수가 존재하지만,
2번째 이동부터는 2가지 이동 가짓수가 존재하는 것이다. 

결국 10번의 이동 가짓수를 따져보면
4 *  ( 2 ^ 9 ) = 2048 가지수.가 되는 것이다.

< 모든 방향을 만들어보기 : 비트마스크 > -------------------------

위, 오, 아, 왼
이라는 4개의 방향을 숫자로 표현할 수 있다
0   1   2    3

이것을 이어붙이면
위, 오, 아, 왼쪽으로 이동시켰다면
0 1 2 3
이라는 숫자를 만드는 것과 같고

이는 4진법의 표현이다.

4진법은, 2개의 2진법의 조합으로 표현할 수 있다.
왜 ?? 이진법에서는 2자리가, 0 ~ 3 이라는 숫자를 의미하기 때문이다.

그러므로, 
비트마스크로 2 ^ 20 을 만든 다음에,

해당 숫자를 2개씩 묶으면
그것이 바로 4진법의 수가 된다.

2개 묶을 때, 앞의 1은 2 , 뒤의 1은 1

ex) 다음과 같다

1 (0 1) (1 0) (1 1) (1 0)  ( 2개씩 묶게 된다면 )
1     1     2     3     2

해당 녀석을 코드로는 어떻게 구현할까?
맨 뒤 2자리씩 비교를 한다.
맨 뒤 2자리 & &3 을 하게 되면, 4진법으로 표현이 될 것이고
왼쪽으로 2번 더 이동해주기 위해서 << 2 를 실시하게 된다.

< 문제에 나와 있는 대로 시뮬레이션 하기 > ----------------------
1) 빨간 공, 파란 공 동시에 이동시키기.

동시에 이동시킨다는 조건이 매우 까다롭다.
사실 코드상으로 동시에 이동시킬 수 는 없기 때문에
우리가 순서를 정해주어야 한다.

빨간색을 먼저, 파란색을 2번째로 이동시킨다고 해보자.
그런데 이 경우에, 이동 횟수 및 방향에 제한이 생길 수 있다.

예를 들어, Red와 Blue 공이 있다고 해보자.
Red가 왼쪽, Blue가 오른쪽에 있고
오른쪽으로 기울이려고 하는데

Red가 Blue에 막혀, 온전히 오른쪽 옆으로 이동하지 못하는 경우가 생긴다는 것이다.
이 경우에는
1) Red를 Blue 전까지 오른쪽 이동
2) Blue 오른쪽 끝까지 이동
3) Red도 마저 오른쪽으로 이동시키기

즉, "기울임" 이라는 행위에는,
다음과 같은 요소들이 필요해진다.

빨 이동 + 파 이동 + 무한 반복 !
언제까지 ?
두 구슬의 위치가 변하지 않을때까지 !


'''

# 오, 왼, 위, 아래 ( 구슬의 이동 방향 )
# x는 행, y는 열
sys.setrecursionlimit(100000)


# 오, 왼, 위, 아래 ( 구슬의 이동 방향 )
# x는 행, y는 열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

LIMIT = 10


class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved
        self.hole = hole
        self.x = x
        self.y = y


def gen(k):
    # 이진법 표현을 ? 10진수 k를 ?
    # 4진법 표현으로 변화시키는 것  : 비트 마스크 방법을 활용한다
    a = [0] * LIMIT
    for i in range(LIMIT):
        # 2자리 단위로 비교한다
        a[i] = (k & 3)
        # 2자리 단위 비교후, 왼쪽으로 2칸 또 이동한다
        # 우리가 비교하려는 값은 왼쪽 2칸 이동후의 값이지만
        # 해당 왼쪽 2칸을 접근하게 하려면, 원래 값 k를 오른쪽으로 2칸 이동시킨다
        k >>= 2
    return a

# simulate : 구슬 "하나"의 이동 , 언제까지 ? 더이상 이동할 공간이 없을 때까지
# x, y 는 구슬의 위치


def simulate(a, k, x, y):
    n = len(a)
    m = len(a[0])
    # 구슬이 있어야 하는데 빈칸이다 ? 이런 경우가 있나 ?
    # ㅇㅇ 이런 경우 있지. 왜냐하면 우리는 dirs라는 방향 정보에는 우선 모든 종류의 방향 정보를 담고 있으니까
    # 즉, dirs 안의 정보를 처리하는 것만으로는, 현재 dirs 정보로 이동시키는 구슬이 구멍에 빠졌는지, 안빠졌는지 알 수 없다.
    # 맨 아래에서 ch == '0', 즉, '빈공'일 경우, 아예 해당 공을 보드에서 빼주도록 처리했다
    # 그 다음 다시 해당 공에 대해서 simulate 함수를 돌릴 때는
    # 이렇게 바로 이미 공이 빠졌음을 return 시켜서 아래의 과정을 거치지 않게 해주는 것이다
    if a[x][y] == '.':
        return Result(False, False, x, y)
    # return 될때, 이동을 하고 끝나는 건지. 처음부터 이동 자체를 안했는지 등등
    moved = False
    while True:
        # 현재 방향 정보 k
        # k방향으로 이동후 변경된 위치 nx, ny
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어났을 때. 더이상 이동을 할수 없다
        # ( 구슬 하나가 왼쪽으로 쭉 ~ 이동한다는 것은, 한칸한칸 이동한다는 것이다 )
        # 그래서 이동했는지 여부 와, 구멍에 빠졌는지 아닌지( 여기서는 False 일 것이다)를 return해준다
        # 사실 모든 벽의 가장자리가 # 이라는 조건이 있기 때문에, return False 해주면 된다
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return Result(moved, False, x, y)
        ch = a[nx][ny]
        # 벽이면, 이동 불가하므로, return
        if ch == '#':
            # nx,ny가 아니라, x와 y를 return 해준다는 것을 잘 봐야 한다
            # 다음이 벽이면, 일단 현재에서 멈춰야 하기 때문이다
            return Result(moved, False, x, y)
        # 구슬일때도, 사실, 앞의 구슬이 이동이 끝나서, 그곳에 있는건지, 아직 이동할 수 있는데 이동하지 않은 건지 알 수 없다. 그래서 일단 stop
        elif ch in 'RB':
            # 마찬가지로, 다음이 구슬이면 일단 멈춰야 한다.
            return Result(moved, False, x, y)
        # 구슬이 빈칸이라면 ?? 항상 이동할 수 있는 것이다
        elif ch == '.':
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x, y = nx, ny
            moved = True
        # 구멍으로 빠졌을 경우, 더 이상 이동하면 안되기때문에 ! return
        # 오직 이 경우에만 return !
        elif ch == 'O':
            # 만약 빠졌다면, 보드에서 아예 해당 구슬을 빼버리는 것
            # ch는 nx,ny 하지만, 여기서 주의할점은 a[x][y] 가 아니라, a[nx][ny]를 빼준다는 점 !!
            # 파란색이던, 빨강색이던
            # 왜??? 빨강공 입장에서도, 파랑공 입장에서도
            # 다른 공이 구멍에 빠졌는지는 모른다.
            # 그래서 일단 자기가 공에 빠지면, 공에 빠진 처리를 해주고
            a[x][y] = '.'
            moved = True
            # 얘는 왜 또 nx, ny가 아니라, x, y 일까  ?

            return Result(moved, True, nx, ny)

# a   : 보드 >> 여기서 중요한 것은, 보드 자체를 변화시켜서는 안된다는 것이다. ( check 함수는 계속 반복될 것이기 때문이다  )
# dir : 방향을 순서대로 이동시키기


def check(a, dirs):
    n = len(a)
    m = len(a[0])
    # 구멍, 빨강, 파랑의 위치를 찾는다
    hx, hy = 0, 0
    rx, ry = 0, 0
    bx, by = 0, 0

    for i in range(n):
        for j in range(m):
            if a[i][j] == 'O':
                hx, hy = i, j
            elif a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j

    # 실제 dirs에 입력된 정보대로, 이동시키기
    cnt = 0
    hole1 = hole2 = False
    # 현재 방향 : k , dirs는 항상 10개의 요소를 갖고 있다 ( 10번의 이동 )
    for k in dirs:

        # for문 한번 == 기울임 1번
        cnt += 1

        # 아래 while문은 실제 이동 처리
        while True:
            # a 보드에서 rx, ry에 있는 보드를 k 방향으로 이동시키기
            p1 = simulate(a, k, rx, ry)
            rx, ry = p1.x, p1.y
            p2 = simulate(a, k, bx, by)
            bx, by = p2.x, p2.y

            # 기울임 같은 경우에는, 빨강 먼저, 그 다음 파랑 이동
            # p1, p2둘다 이동하지 않았다면, 더이상 이동할 필요가 없는 것 => break 시키기
            if not p1.moved and not p2.moved:
                break
            if p1.hole:
                hole1 = True
            if p2.hole:
                hole2 = True

    # simulate 함수가 return하는 것 : 1) 이동했는가 ? 2) 구멍에 빠졌는가
    # 빨강 구슬만 구멍에 빠져야 한다. 즉, hole1 만 true가 되어야 한다
    # 이 경우에 대비하여, hole2가 true라는 것은, 파랑도 빠졌다는 것이므로, return -1
        # 그런데, 이렇게 구멍 빠졌는지 여부를 검사하는 것을 왜
        # 이동에 대한 처리를 while을 통해 다 돌리고 마지막에 와서야 하게 되는 것일까?
        # 빨강 구멍 여부만 보는 것이 아니라, 파랑도 봐야 한다
        # 그래서, 일단 다 이동을 쫙 시켜보고, 마지막에 와서 보는 것이다
        if hole2:
            return -1
        if hole1:
            return cnt

    # for문을 통과하여, 여기까지 내려왔다는 것은
    # 10번 안에 답을 찾지 못하였다는 것이다
    return -1


def valid(dirs):
    l = len(dirs)
    for i in range(l-1):
        # 아래 if문 4개는 서로 반대방향이라는 것 false
        if dirs[i] == 0 and dirs[i+1] == 1:
            return False
        if dirs[i] == 1 and dirs[i+1] == 0:
            return False
        if dirs[i] == 2 and dirs[i+1] == 3:
            return False
        if dirs[i] == 3 and dirs[i+1] == 2:
            return False
        # 같은 방향일 때도 false
        if dirs[i] == dirs[i+1]:
            return False
    return True


n, m = map(int, input().split())
original = [input() for _ in range(n)]
ans = -1

# 모든 방법 만들기( 00000000000000000.... ~ 11111111111..... )
# 총 2 ^ 20 > 왜 2^20 일까? 왜냐하면, 4가지 방향의 이동, 최대 10번 이동 == 4 ^ 10 == 2 ^ 20 이기 때문이다
for k in range(1 << (LIMIT * 2)):

    # 우리는 현재 이동할수 있는 모든 경우의 수를 고려하고 있는 것이고
    # gen(k)를 통해서, 모든 해당 경우의 수를 4진법으로 바꿔서, 해당 경우의 수를 처리하고 있는 것이다
    dirs = gen(k)  # 0,1,2,3 으로 이루어진 4진법으로 바꾼다.

    # 올바른 방법이 아니라면, 건너뛴다.
    if not valid(dirs):
        continue

    # 왜 여기서 따로 a를 새로 만들어주는 것일까?
    # 말했듯이, 각 dirs 한번 마다, 보드를 처음부터 새롭게 쓸 것인데
    # original이라는 원래 데이터 자체를 넘겨줘버리면, 이후 dirs 검사, 즉, 이후 for문 검사에서 정확한 데이터 검사가 일어나지 않게 될 것이다
    a = [list(row) for row in original]

    # a를 해당 dirs 방향으로 이동시킨다
    # cur : 빨간 구슬만 구멍에 빠지기 까지의 횟수
    cur = check(a, dirs)

    if cur == -1:  # 만약, 빨간 구슬만 구멍에 빠지는 경우가 없다면
        continue
    if ans == -1 or ans > cur:
        ans = cur

print(ans)


'''
C++

#include <iostream>
#include <vector>
#include <string>
using namespace std;
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
const int LIMIT = 10;
vector<int> gen(int k) {
    vector<int> a(LIMIT);
    for (int i=0; i<LIMIT; i++) {
        a[i] = (k&3);
        k >>= 2;
    }
    return a;
}
pair<bool,bool> simulate(vector<string> &a, int k, int &x, int &y) {
    if (a[x][y] == '.') return make_pair(false, false);
    int n = a.size();
    int m = a[0].size();
    bool moved = false;
    while (true) {
        int nx = x+dx[k];
        int ny = y+dy[k];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
            return make_pair(moved, false);
        }
        if (a[nx][ny] == '#') {
            return make_pair(moved, false);
        } else if (a[nx][ny] == 'R' || a[nx][ny] == 'B') {
            return make_pair(moved, false);
        } else if (a[nx][ny] == '.') {
            swap(a[nx][ny], a[x][y]);
            x = nx;
            y = ny;
            moved = true;
        } else if (a[nx][ny] == 'O') {
            a[x][y] = '.';
            moved = true;
            return make_pair(moved, true);
        }
    }
    return make_pair(false, false);
}
int check(vector<string> a, vector<int> &dir) {
    int n = a.size();
    int m = a[0].size();
    int hx,hy,rx,ry,bx,by;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (a[i][j] == 'O') {
                hx = i; hy = j;
            } else if (a[i][j] == 'R') {
                rx = i; ry = j;
            } else if (a[i][j] == 'B') {
                bx = i; by = j;
            }
        }
    }
    int cnt = 0;
    for (int k : dir) {
        cnt += 1;
        bool hole1=false, hole2=false;
        while (true) {
            auto p1 = simulate(a, k, rx, ry);
            auto p2 = simulate(a, k, bx, by);
            if (p1.first == false && p2.first == false) {
                break;
            }
            if (p1.second) hole1 = true;
            if (p2.second) hole2 = true;
        }
        if (hole2) return -1;
        if (hole1) return cnt;
    }        
    return -1;
}
bool valid(vector<int> &dir) {
    int l = dir.size();
    for (int i=0; i+1<l; i++) {
        if (dir[i] == 0 && dir[i+1] == 1) return false;
        if (dir[i] == 1 && dir[i+1] == 0) return false;
        if (dir[i] == 2 && dir[i+1] == 3) return false;
        if (dir[i] == 3 && dir[i+1] == 2) return false;
        if (dir[i] == dir[i+1]) return false;
    }
    return true;
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    int ans = -1;
    for (int k=0; k<(1<<(LIMIT*2)); k++) {
        vector<int> dir = gen(k);
        if (!valid(dir)) continue;
        int cur = check(a, dir);
        if (cur == -1) continue;
        if (ans == -1 || ans > cur) ans = cur;
    }
    cout << ans << '\n';
    return 0;
}

'''
