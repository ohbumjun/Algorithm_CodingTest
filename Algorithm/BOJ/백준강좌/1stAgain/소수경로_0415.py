# https://www.acmicpc.net/problem/1963

import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
< 기본 개념 >
각 숫자를 '정점'
각 숫자까지 가는 것을 '간선'
한번에 change 가능 => '간선' 길이 1
최소 거리 구하기
단, 소수인 정점만 갈 수 있음

따라서 "BFS + 소수개념" 조합 


1. 에라토스 테네스의 체 -> 모든 소수 세팅하기
- 소수란, 2부터 존재한다는 것도 알`아야 한다
- 제곱근 까지만, 수를 고려해도 된다 

2. 입력숫자 로 시작하기
- 매번 다음 가능한 숫자
- 4자리만 가능 --> 맨 앞 0인 경우는 -1 return 해주기

3. 리턴받은 숫자가 -1이면 다시
- 해당 숫자가 소수이고, 방문한적이 없다면
queue에 넣고, dist 1 증가시켜주고 

'''


def nextNum(num, idx, newN):
    # num 숫자의 idx 번째 자리에 newNd을 넣고 싶다
    # 맨 앞 0이 들어오는 경우 skip
    if idx == 0 and newN == 0:
        return -1
    num = list(str(num))
    num[idx] = newN
    num = ''.join(map(str, num))
    return int(num)


prime = [True] * 10001
# 소수 세팅
for i in range(2, 10001):
    if prime[i] == True:
        for j in range(i+i, 10001, i):
            if j <= 10000:
                prime[j] = False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # BFS를 위한 distance, Check 배열 초기화
    d = [0] * 10001
    c = [False] * 10001
    d[n] = 0
    c[n] = True
    q = deque([n])
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = nextNum(now, i, j)
                if nxt != -1:
                    if prime[nxt] == True and c[nxt] == False:
                        c[nxt] = True
                        d[nxt] = d[now] + 1
                        q.append(nxt)
    print(d[m])
