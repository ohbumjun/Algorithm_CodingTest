#  https://www.acmicpc.net/status?user_id=dhsys112&problem_id=14391&from_mine=1

import itertools
from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

# N : 행, M : 열
N, M = map(int, input().split())
paper = [list(map(int, input())) for _ in range(N)]

# itertools.product : 2개 이상의 리스트의 모든 조합 구할 때 사용
'''
a = itertools.product([0,1],repeat = 2)
a = list(a)
print(a)
--> 결과 : [(0, 0), (0, 1), (1, 0), (1, 1)]
'''
# 각칸은 2개의 상태를 갖는다
# 0 : 가로로 자르는 상태
# 1 : 세로로 자르는 상태
# 따라서 총 경우의 수는 2^(N*M) 개가 될 것이다.
# 왜냐하면 총 칸의 개수가 N*M 개 이기 때문이다

# 1) 비트마스크를 2차원 리스트로 만든다
# 2) 가로 : 0을 만나면 , 진짜 값 저장 , 옆으로 가고
#       또 0이면 , 이전 것에 10을 곱해주고 저장
#       만약 , 1을 만나면, 합계에 저장해주고, 저장한 거 0으로
#       만들고 , 다시 시작, 만약에 맨 마지막 열을 만나면 그냥 저장 //
# 3) 세로 : 가로와 마찬가지로 만든다

ans = 0
a = itertools.product([0, 1], repeat=N*M)

# 1d를 2d matrix로 바꿔주기


def to_matrix(one_d, col):
    return [one_d[i:i+col] for i in range(0, len(one_d), col)] 


for x in a:
    # 2차원 행렬
    bit_mask = to_matrix(x, M)
    sumh = 0

    # r : 행
    for r in range(N):
        hori = 0
        # c : 열
        for c in range(M):
            if bit_mask[r][c] == 0:
                hori = 10 * hori + paper[r][c]
            if bit_mask[r][c] == 1 or c == M-1:
                sumh += hori
                hori = 0
    sumv = 0
    for c in range(M):  # 열
        cori = 0
        for r in range(N):  # 행
            if bit_mask[r][c] == 1:
                cori = 10 * cori + paper[r][c]
            if bit_mask[r][c] == 0 or r == N-1:
                sumv += cori
                cori = 0
    sum_all = sumh + sumv
    ans = max(sum_all, ans)

print(ans)
