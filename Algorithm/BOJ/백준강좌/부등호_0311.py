# https://www.acmicpc.net/problem/2529

''' ------------------------------------------------------------------
'브루트 포스' : '순열' 문제

왜 ?? 이미 선택된 수는 '모두 달라야 한다' 라는 조건이 있기 때문이다.
순열이라는 것은, 
중복되지 않은 수로, 순서를 섞어서 
만들 수 있는 수열을 모두 구하면서 해결 할 수 있다.

이 문제 같은 경우는
k + 1 개의 수가 있고,
0 ~ 9 중에서 k + 1을 고르고
그 중에서, 순서를 고려해야 한다.
( 즉, 기본 순열문제와의 차이점은
보통 순열은 숫자가 주어지고, 섞어라 ! 라는 식의 문제인데,

여기서는, 숫자 자체를 우리가 뽑는 과정도
추가적으로 들어가 있다라는 것이다.
)

하지만, 사실 '고르는 부분'을 뺄 수 있다.



가장 작은 수는
0부터 k+1 개의 수까지 ( ex. 1 2 3 4 5 )

가장 큰수는
9까지 k+1개 ( ex. 9 8 7 6 5 )

"수의 크기" ( 작다 / 크다 )

수의 길이는 k + 1 로 동일하므로
수의 대소 비교를 할때, 문자열의 대소와 동일하다.
ex) '3' < '23'은 꼭 정수로 바꾸지 않아도, 대소관계 비교가 바로 가능하다.

가장 작은 수 : 0부터 k+1 개의 수를 활용하여 , 
첫순열 ( 가장 작은 수 )을 만들고, 계속 다음 순열, 다음 순열 찾다가
부등호 관계 만족하는 것이 나오면, 그것이 '답' ( 가장 작은 수)

가장 큰 수 : 9까지 k+1개의 수를 고르고
마지막 순열( 가장 큰 수 )을 고른 다음
> 이전, 이전 
이때 부등호 관계가 만족한다면, 그것이 '답' ( 가장 큰 수 )



** 시간 복잡도 **
k + 1개의 칸을 채우기 : ( k + 1 ) !
k : 각 칸을 채울 때마다 K개의 수를 살피기 때문이다.

'''

import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


def next_permutation(arr):
    inverse_point = len(arr) - 2
    while inverse_point >= 0 and arr[inverse_point] > arr[inverse_point + 1]:
        inverse_point -= 1
    if inverse_point < 0:
        return False
    j = len(arr) - 1

    while arr[j] < arr[inverse_point]:
        inverse_point -= 1

    arr[j], arr[inverse_point] = arr[inverse_point], arr[j]

    j = len(a) - 1
    while inverse_point < j:
        a[inverse_point], a[j] = a[j], a[inverse_point]
        inverse_point += 1
        j -= 1

    return True


def prev_permutation(arr):
    inverse_point = len(arr) - 2

    while inverse_point >= 0 and arr[inverse_point] < arr[inverse_point + 1]:
        inverse_point -= 1

    if inverse_point < 0:
        return False

    j = len(arr) - 1

    while arr[j] > arr[inverse_point]:
        j -= 1

    arr[j], arr[inverse_point] = arr[inverse_point], arr[j]

    j = len(a) - 1

    while inverse_point < j:
        a[inverse_point], a[j] = a[j], a[inverse_point]
        inverse_point += 1
        j -= 1

    return True

# perm : 현재 우리가 보고 있는 순열
# a : 부등호 기호


def check(perm, a):
    for i in range(len(a)):
        if a[i] == '<' and perm[i] > perm[i+1]:
            return False
        if a[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True


k = int(input())
a = input().split()`
small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]


while True:
    if check(small, a):
        break
    if not next_permutation(small):
        break

while True:
    if check(big, a):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
