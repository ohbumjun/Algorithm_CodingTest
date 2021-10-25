# https://www.acmicpc.net/problem/5904


from copy import deepcopy
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
# 각 s[idx] 별, 새로운 moo의 길이 --> s[0] : moo == 3 , s[1] : mooo == 4, s[2] : moooo == 5
ptL = {}
# 각 s[idx] 총 길이
ttL = {}
ptL[0] = 3
ttL[0] = 3
cIdx = 0

isM = False

while True:
    if N <= ttL[cIdx]:
        # 이제부터 찾기
        break
    ptL[cIdx+1] = ptL[cIdx] + 1
    ttL[cIdx+1] = ttL[cIdx] * 2 + ptL[cIdx+1]
    cIdx += 1

while True:
    if cIdx == 0:
        if N == 1:
            isM = True
        else:
            isM = False
        break
    # ex) moo mooo moo 라고 할 때
    # 1) 앞쪽 부분에 N이 있을 때 : 즉, 앞 moo 범위 안에 N이 있을 때( N <= 3)
    # 1) 중간쪽 부분에 N이 있을 때 : 즉, 중간 mooo 범위 안에 N이 있을 때( 4 <= N <= 7)
    # 1) 뒷쪽 부분에 N이 있을 때 : 즉, 뒤 moo 범위 안에 N이 있을 때( 8 <= N <= 11)
    if N <= ttL[cIdx-1]:
        cIdx -= 1
        continue
    # 중간
    elif N - ttL[cIdx-1] <= ptL[cIdx]:
        diff = N - ttL[cIdx-1]
        if diff == 1:
            isM = True
        else:
            isM = False
        break
    # 뒷쪽
    else:
        N -= (ttL[cIdx-1] + ptL[cIdx])
        cIdx -= 1
        continue
print('m' if isM else 'o')
