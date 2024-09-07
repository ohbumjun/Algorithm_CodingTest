# https://www.acmicpc.net/problem/20056

from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
table = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    table[r-1][c-1].append((m, s, d))

print("init")
for t in table:
    print(t)

for _ in range(K):
    table_c = [[[] for _ in range(N)] for _ in range(N)]
    # 이동 처리
    for r in range(N):
        for c in range(N):
            for elem in table[r][c]:
                m, s, d = elem
                ns = s % N
                nr, nc = r+ns*dx[d], c+ns*dy[d]
                if nc >= N:
                    nc -= N
                if nc < 0:
                    nc += N
                if nr >= N:
                    nr -= N
                if nr < 0:
                    nr += N
                table_c[nr][nc].append((elem))
    print("after move")
    for t in table_c:
        print(t)

    # 파이어볼 합치기
    for r in range(N):
        for c in range(N):
            if len(table_c[r][c]) > 1:
                len_e = len(table_c[r][c])
                t_m, t_s, t_d = 0, 0, 1
                rest_d = table_c[r][c][0][2] % 2
                # 질량 합, 속력 합, 방향 여부 구하기
                for sp in range(len_e):
                    t_m += table_c[r][c][sp][0]
                    t_s += table_c[r][c][sp][1]
                    if rest_d != (table_c[r][c][sp][2] % 2):
                        t_d = -1  # 모두 홀수 혹은 모두 짝수가 아님
                e_m = t_m // 5
                e_s = t_s // len_e
                if e_m == 0:
                    table_c[r][c] = []
                    continue
                # 1이면, 0,2,4.6 에서 시작
                # -1이면, 1,3,5,7
                s_d = 0 if t_d == 1 else 1
                tmp = []
                for _ in range(4):
                    tmp.append((e_m, e_s, s_d))
                    s_d += 2
                table_c[r][c] = tmp
    print("after divide")
    for t in table_c:
        print(t)
    print()

    table = table_c

# 남아있는 파이어볼 질량의 합 구하기
# print("end")
# for t in table : print(t)
res = 0
for r in range(N):
    for c in range(N):
        for elem in table[r][c]:
            res += elem[0]
print(res)
