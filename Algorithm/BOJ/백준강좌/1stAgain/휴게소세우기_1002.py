# https://www.acmicpc.net/problem/1477

# 헷갈리면 안되는 것
# 하나씩 휴게소를 설치하는 것이 아니라
# 한번에 M개의 휴게소를 설치해야 한다

import itertools
from copy import deepcopy
import heapq
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

N, M, L = map(int, input().split())
rests = list(map(int, input().split()))
rests.append(0)
rests.append(L-1)
rests.sort()


def count(n):
    num = 0
    for i in range(1, N+2):
        if (rests[i] - rests[i-1] - 1) < n:
            continue
        num += (rests[i] - rests[i-1] - 1) // n
    print("num : ", num)
    return num


st = 0
ed = L-1
ans = 0


while st <= ed:
    # mid : 휴게소 간격 길이
    mid = (st+ed) // 2
    # 해당 mid 값으로 놓을 수 있는 휴게소 개수
    cnt = count(mid)
    # print("mid",mid)
    if cnt <= M:
        ed = mid - 1
        ans = mid
    else:  # mid 길이를 늘려야 한다는 것인데
        st = mid + 1
print(ans)
