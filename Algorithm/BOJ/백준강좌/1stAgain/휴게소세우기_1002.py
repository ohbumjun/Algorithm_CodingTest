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
        # 왜 -1을 해주는 것일까 ? 여기에서 n이란, 휴게소를 세울 간격이다
        # 그런데, 휴게소를 겹치게 세우면 안된다
        # 다시 말해서, 0부터 n씩 더해가는데, 그 과정에서, 기존의 휴게소 위치에 놓이면 안된다는 것이다
        # 그런데 만약 rests[i]-rests[i-1] 을 나눠서 더해주면
        # ex) 100, 200, 300
        # n : 100 --> 겹치게 놓일 수 있다
        # 따라서, 미리 이런 사항을 방지하기 위해 애초부터 -1을 빼주고 더해주는 것이다
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
    else:  # mid 길이를 늘려야 한다
        st = mid + 1
print(ans)
