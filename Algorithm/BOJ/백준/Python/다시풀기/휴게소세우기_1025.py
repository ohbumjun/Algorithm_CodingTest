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

# 인터넷 상의 많은 해결책들이 L 이 아니라 L-1을 넣으라고 한다
# 왜냐하면 마지막 구간에는 설치할 수 없으니까
# 그런데, 우리는 count 코드를 보면 -1 을 추가적으로 해준다
# 즉, 절대 겹치기 않게 휴게소를 설치하고 있고
# 이는 곧, 마지막 지점에서도 겹치지 않는 다는 점이다
# 따라서 L-1이 아니라, L-1을 해주어야 한다
rests.append(L)
rests.sort()


def count(n):
    num = 0
    for i in range(1, N+2):
        # 왜 -1을 해주는 것일까 ? 여기에서 n이란, 휴게소를 세울 간격이다
        # 그런데, 휴게소를 겹치게 세우면 안된다
        # 다시 말해서, 0부터 n씩 더해가는데, 그 과정에서, 기존의 휴게소 위치에 놓이면 안된다는 것이다
        # 그런데 만약 rests[i]-rests[i-1] 을 나눠서 더해주면
        # ex) 100, 200, 300
        # n : 100 --> 겹치게 놓일 수 있다
        # 따라서, 미리 이런 사항을 방지하기 위해 애초부터 -1을 빼주고 더해주는 것이다
        num += (rests[i] - rests[i-1] - 1) // n
    # print("num : ", num)
    return num


st = 1  # 0이 아니라 1로 시작해주어야 한다
# 그래야 zero division error가 나지 않는다
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
