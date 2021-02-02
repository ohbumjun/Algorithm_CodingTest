# https://www.acmicpc.net/problem/1874

import sys
sys.stdin = open("input.txt", "rt")
import heapq as hq
from collections import deque

n = int(input())
res = []
stack = []
flag  = True
cnt   = 0

for i in range(n):
    inputNum = int(input())
    # 입력값만큼 cnt 증가시키면서, stack에 차례대로 쌓기 , + 출력, cnt 증가
    # 여기서 cnt < inputNum에서 등호가 붙지 않는 것
    # cbt += 1가 바로 다음줄에 와야 하는 것이 중요하
    while cnt < inputNum:
        cnt += 1
        stack.append(cnt)
        res.append('+')

    # 만약 stack 맨 위의 값이, input과 다르다면 : false
    if stack[-1] != inputNum :
        flag = False
        exit(0)
    # 같다면, pop 하고,  - 출력
    else:
        stack.pop()
        res.append('-')

if flag == False:
    print("NO")
else:
    for x in res :
        print(x)
