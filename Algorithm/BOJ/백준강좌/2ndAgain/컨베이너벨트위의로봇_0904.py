# https://www.acmicpc.net/problem/20055

from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

# 로봇은 "올리는 위치에만" 올린다
n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
ans = 1

robot = deque([0]*(n*2))

while True:
    # 1 : 벨트 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    # 2 : 로봇 회전
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    robot[n-1] = 0

    # 3. 올리기
    if belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    # 4. 내구도 검사 ----햣
    s = 0
    for i in range(2*n):
        if belt[i] == 0:
            s += 1
    if s >= k:
        print(ans)
        exit()
    ans += 1
