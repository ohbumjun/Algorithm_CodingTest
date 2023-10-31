# https://www.acmicpc.net/problem/6603
from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

dic = defaultdict(int)


def go(arr, tmp, ch, num):
    if num == 6:
        tmp.sort()
        if dic[str(tmp)] != 0:
            return
        dic[str(tmp)] = 1
        print(' '.join(map(str, tmp)))
        return
    l_arr = len(arr)
    for i in range(l_arr):
        if ch[i] == 0:
            ch[i] = 1
            go(arr, tmp+[arr[i]], ch, num+1)
            ch[i] = 0


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    ch = [0] * len(arr)
    go(arr, [], ch, 0)
    print()
