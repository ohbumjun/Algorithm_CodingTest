# https://www.acmicpc.net/problem/1891

from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

# 1,2,3,4 idx는 각각 1,2,3,4 분면에서의 출발 x,y 좌표를 의미
dx = [-1, 0, 0, 1, 1]
dy = [-1, 1, 0, 0, 1]

# 우리는 사분면을 하나의 이차원 배열로 보고 시작할 것이다.
n, digit = map(int, input().split())
mv_y, mv_x = map(int, input().split())
sr, sc = 0, 0
length = 2**n

# 나눌때마다 시작 위치 지정
st = length // 2

# 주어진 digit 각각의 숫자를 접근하기 위한 idx
idx = 0

# digit의 각 숫자에 접근하기 위해 str로 전환
s_digit = str(digit)
for _ in range(n):
    cNum = int(s_digit[idx])  # 3,4,1
    sr += (st * dx[cNum])
    sc += (st * dy[cNum])
    st //= 2
    idx += 1
    # 최종 sr,sc : 341 이라는 숫자가 사분면에서 위치한 x,y좌표

# print("sr,sc",sr,sc)
# 존재하지 않는 사분면일 경우
if 0 > sr or sr >= length or 0 > sc or sc >= length:
    print(-1)
    exit()

# 좌표 이동
# mv_x의 경우 -을 해준다. 위로 올라가는 경우, mv_x가 양수라고 했으므로
nr, nc = sr-mv_x, sc+mv_y
# print("nr,nc",nr,nc)
if 0 > nr or nr >= length or 0 > nc or nc >= length:
    print(-1)
    exit()


def checkNum(ix, iy):
    if ix == 0 and iy == 1:
        return 1
    if ix == 0 and iy == 0:
        return 2
    if ix == 1 and iy == 0:
        return 3
    if ix == 1 and iy == 1:
        return 4


# 이제는 반대의 과정( 좌표 --> 숫자 알아내기 )
st_div = length // 2
ans = ''

for _ in range(n):
    x_div, y_div = nr // st_div, nc // st_div
    ans += str(checkNum(x_div, y_div))
    nr, nc = nr % st_div, nc % st_div
    st_div //= 2

print(ans)
