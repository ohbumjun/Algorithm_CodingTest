# 간편 설명
'''
이는 array의 possible한 subsum 들의 개수를 구하는 문제와 같다 

특정 arr의 subsum을 구한다는 것은, 
다른 말로 하면, 부분집합을 구한 이후, 그 해당 부분집합 각각의 원소들의 합을 구하는 것과 같다

다른 말로 하면, 사실, 부분집합을 구하는 것이다

1) Brute Force
- 부분집합을 구한다는 것은, 각각의 원소가 부분집합에 속할지 안속할지를 결정한다는 것
즉, n개의 원소가 있다면 각각의 원소에 대해서 
1. 속할지 2. 안속할지 --> 를 결정하는 것과 같다는 것이다 

따라서 2 ^ n 만큼의 시간이 소요된다

2) Meet in the middle
maximum subsum array를 구할 때 사용하는 개념이다 

해당 n개의 원소를 반으로 쪼갠다
A : [0 ~ n//2]
B : [n//2 + 1 ~ n]

각각의 subsum들을 구하여,
각각의 subsumA, subsumB 라는 array 에 넣는다

subsumB를 sort 한다

subsumA 내 각각의 원소에 대해서 ,
sort된 subsumB를 이진 탐색 하여 , 
최대의 maximum을 구하는 과정을 진행하면 된다 

'''

import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

n, c = map(int, input().split())
a = list(map(int, input().split()))
res = 0

midLen = len(a) // 2

subA = a[:midLen]
sSumA = []
subB = a[midLen:]
sSumB = []


def subSum(L, idx, sum, arr, sSumA):
    if L == idx:
        sSumA.append(sum)
        return
    else:
        # 선택
        subSum(L, idx+1, sum + arr[idx], arr, sSumA)
        # 선택 x
        subSum(L, idx+1, sum, arr, sSumA)


def upperBound(st, ed, target, a):
    # 1) ed
    # 2) a[mid] < target , a[mid] == target  --> 같은 알고리즘
    '''
    [2,4,4,7,9]
    a[4]
    a[5]

    target = 10

    '''
    while st < ed:
        mid = (st+ed) // 2
        if a[mid] <= target:
            # target보다 큰 값을 지닌 원소를 찾아 계속 뒤로
            st = mid + 1
        elif a[mid] > target:
            ed = mid
    return ed


subSum(len(subA), 0, 0, subA, sSumA)
subSum(len(subB), 0, 0, subB, sSumB)
sSumB.sort()

for elem in sSumA:
    # c = 10 , elem = 4 , 6 target
    target = c - elem
    if c - elem < 0:
        continue
    # 여기서 끝의 위치를 의미하는 2번째 인자로, 일반적인 binary와 달리
    # len(sSumB) - 1 을 넣어주면 안된다
    # ex) [0,1] => '1'까지 가능하다면, 2라는 숫자가 return되어야 하는데
    # 애초부터 len(sSumB) - 1 을 넣어주게 되면, 최대 1이라는 숫자밖에 return 되지 않는다

    # c : 10
    # sSumA => 1
    # sSumB = [3,5,8] --> binary(0,2)

    add = upperBound(0, len(sSumB), target, sSumB)
    res += add
print(res)
