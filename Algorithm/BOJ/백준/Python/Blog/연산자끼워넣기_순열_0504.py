# https://www.acmicpc.net/problem/14888

import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
먼저 모든 수열을 입력받고,

순열을 만들어 저장할 배열을 설정한다
+ 0, - 1, * 2, // 3 으로 설정한다.

각 순열 조합에 대한, 결과들을
배열에 모두 저장해서

그 중에서 최대, 최소를 선택하면 된다

즉, 특정 순열에 대한, 결과값이 각각 다르게 나올 것이라는 것이다. 

'''


def next_permutation(a):
    i = len(a) - 1
    # 여기서는 next_permutaion할 때 등호 비교를 꼭 포함시켜줘야 한다
    # 왜냐하면, 실제로 a에 중복된 값이 존재하기 때문이다
    while i > 0 and a[i-1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(a) - 1

    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def div(a, b):
    if a >= 0:
        return a // b
    else:
        return -(- a // b)


def cal(arr, d):
    now = arr[0]
    for i in range(len(d)):
        if d[i] == 0:
            now += arr[i+1]
        elif d[i] == 1:
            now -= arr[i+1]
        elif d[i] == 2:
            now *= arr[i+1]
        else:
            now = div(now, arr[i+1])
    return now


n = int(input())
inputArr = list(map(int, input().split()))
calc = list(map(int, input().split()))
d = []
res = []
for i in range(len(calc)):
    for _ in range(calc[i]):
        d.append(i)

while True:
    now = cal(inputArr, d)
    res.append(now)
    if not next_permutation(d):
        break

print(max(res))
print(min(res))
