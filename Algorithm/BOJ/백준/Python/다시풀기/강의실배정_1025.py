# https://www.acmicpc.net/problem/11000

import itertools
from copy import deepcopy
import heapq
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N = int(input())
classes = []
for _ in range(N):
    st, ed = map(int, input().split())
    classes.append((st, ed))

# 시작 시간 기준 정렬
classes = sorted(classes, key=lambda x: x[0])

# 강의실들이 종료시간이 들어가 있다
room = []

# 첫강의 종료 시간을 넣는다
heapq.heappush(room, classes[0][1])
classes.pop(0)

# 총 nlog(n)
# 순회 : n
# 각 순회에서 heap : log(n)
for cls in classes:
    stT, edT = cls
    # 강의실 내 강의중, 가장 종료시간 빠른 강의를 추출
    minEdT = room[0]
    # 해당 강의 시작시간이, minEdT보다 늦으면, 같은 강의실 내 진행 가능
    # 따라서, 기존 강의 중 종료시간 가장 빠른 강의와 대체
    if minEdT <= stT:
        heapq.heappop(room)
        heapq.heappush(room, edT)
    # 그렇지 않다면, 새로운 강의실 필요
    else:
        heapq.heappush(room, edT)
print(len(room))
