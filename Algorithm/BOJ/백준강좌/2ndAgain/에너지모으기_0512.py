import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
- 에너지 구슬 구하기 경우의 수를 구한다
= 10 팩토리얼
= 3628800

- 각각의 경우에 대해서
하나 고를때마다, 전체 구슬을 다시 접근해야 한다
= n*n
= 100 only

따라서, 10^8 정도이기 때문에
시간 초과는 안걸릴 것 같다 
'''

n = int(input())
a = list(map(int, input().split()))
ways = []
res = -1


def sumE(way, a):
    cnt = 0
    i = 0
    slen = len(way)
    while len(a) > 2:
        cnt += (a[way[0]-1]*a[way[0]+1])
        a.pop(way[0])  # way[i] 번째 idx를 제거한다
        # idx 조정
        # 이 부분이 어렵다. 이미 고려한 idx를 빼고 다시 배열을 재조정 하는 것
        for j in range(1, len(way)):
            if way[j] > way[0]:
                way[j] -= 1
        way.pop(0)
        i += 1
    return cnt


def go(idx, ch, res):
    if idx == n-2:
        ways.append(res)
    else:
        for i in range(1, n-1):
            if ch[i] == 0:
                ch[i] = 1
                go(idx+1, ch, res+[i])
                ch[i] = 0


for i in range(1, n-1):
    ch = [0] * n
    ch[i] = 1
    go(1, ch, [i])

for way in ways:
    a_copy = [x for x in a]
    tmp = sumE(way, a_copy)
    if res == -1 or res < tmp:
        res = tmp
print(res)
