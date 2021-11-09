# https://www.acmicpc.net/status?user_id=dhsys112&problem_id=14889&from_mine=1

import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
해당 문제는,
순열로 풀수 있다.

모든 사람을 순서대로 넣는 것이다.

물론, 각 사람이 어디에 들어가는지는 모르지만
2개의 집단으로
그리고 각각 n // 2명의 사람들이 있는 집단으로
나뉜다는 것은 알 수 있다

0 ~ n - 1 이라는 idx를 각각의 사람이라고 해보자.
b를 집단 배열이라고 하면
b[i]는 i idx 사람이 속한 집단을 의미한다

집단을 0과 1로 나눈다고 해보자.

1) next_permutation 사용을 위해, 최소 순열 초기화 후 시작
2) 각 단계마다, b[i] == 1, b[i] == 0인 2개의 집단을 구분한다.

각각을 first, second라는 집단에 i를 넣는다( 서로 다른 idx 집단이 있을 것이다 )

매 단계마다
first, second 집단의 합을 구하고
그 차이를 구한다

그 차이의 최소를 구한다.

'''


def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n = int(input())
b = [0 if i < n // 2 else 1 for i in range(n)]

arr = [list(map(int, input().split())) for _ in range(n)]
res = 21412389713


'''
# 아래와 같은 코드는 시간초과
# 즉, list slicing이 시간이 오래 걸린다 !
p = [x for x in range(n)]
while True:
    mid = len(p) // 2
    fg = p[:mid]
    fSum = 0
    sg = p[mid:]
    sSum = 0

    for i in range(len(fg)):
        for j in range(len(fg)):
            if i == j : continue
            fSum += s[fg[i]][fg[j]]
            sSum += s[sg[i]][sg[j]]
'''

while True:
    first = []
    one = 0
    second = []
    two = 0

    for i in range(n):
        if b[i] == 0:
            first.append(i)
        else:
            second.append(i)

    # 합 구하기
    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue
            one += arr[first[i]][first[j]]
            two += arr[second[i]][second[j]]

    res = min(res, abs(one - two))

    if not next_permutation(b):
        break

print(res)
