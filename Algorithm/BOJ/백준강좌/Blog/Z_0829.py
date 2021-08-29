# https://www.acmicpc.net/status?user_id=dhsys112&problem_id=1074&from_mine=1

from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N, r, c = map(int, input().split())
stLength = 2**N


# 4개의 영역 중에서, 어떤 영역에 속하는지 판단하기
def judgeArea(r, c):
    if r == 0 and c == 0:
        return 1  # 왼쪽 위
    if r == 0 and c == 1:
        return 2  # 오른쪽 위
    if r == 1 and c == 0:
        return 3  # 왼쪽 아래
    if r == 1 and c == 1:
        return 4  # 오른쪽 아래


# 그 다음 재귀함수로 들어갈때, 새로운 r,c 구하기
def newRC(area, r, c, length):
    if area == 1:
        return (r, c)
    if area == 2:
        return (r, c-length)
    if area == 3:
        return (r-length, c)
    if area == 4:
        return (r-length, c-length)


# 마지막 4칸 남을 때, 몇번째 인지 구하기
def cal(r, c):
    if r == 0 and c == 0:
        return 1
    if r == 0 and c == 1:
        return 2
    if r == 1 and c == 0:
        return 3
    if r == 1 and c == 1:
        return 4


def go(stN, length, r, c):  # length : 8 --> 4 --> 2
    if length == 2:
        res = stN + cal(r, c)
        print(res-1)
        exit()
    div = length // 2  # 그 다음, 판에서, 행 혹은 열의 1/2
    each = div*div     # 그 다음 판에서, 4개로 나눌때, 한 영역의 크기
    area = judgeArea(r//div, c//div)
    stN += (area-1) * each
    r, c = newRC(area, r, c, div)
    go(stN, div, r, c)  # 새로운 시작점 , 새로운 행,열의 정보로 재귀 함수 시작


go(0, stLength, r, c)
