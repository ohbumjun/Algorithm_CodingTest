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

가장 작은 수 : 0부터 k+1 개의 수를 활용하여 , ( ex. 0123)
첫순열 ( 가장 작은 수 )을 만들고, 계속 다음 순열, 다음 순열 찾다가
부등호 관계 만족하는 것이 나오면, 그것이 '답' ( 가장 작은 수)

가장 큰 수 : 9까지 k+1개의 수를 고르고 , ( ex. 9876 )
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

# 다음 크기의 순열을 찾기


def next_permutation(a):
    i = len(a) - 1
    # invere_point를 찾는다
    # 무슨 말이나면, 제일 큰 순열은 뒤로 갈수록 숫자가 작아질 것
    # 다른 말로하면, 앞으로 오면서 숫자가 커질 것
    # 현재 기준, 다음 크기의 순열을 구하기 위해서는
    # 뒤의 숫자보다, 작은 앞의 숫자를 찾고
    # 그 위치를 기준으로 다시 순열을 재정비해야 한다
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    # 이 말은 즉슨, 계속 왼쪽으로 갔다는것
    # 즉, 현재 a로 들어온 순열이 가장 큰 수열에 해당한다는
    if i <= 0:
        return False

    j = len(a) - 1

    # inverespoint를 기준으로, 오른쪽에 있는 숫자중에서
    # inverespoint보다 한단계 더 큰 숫자를 찾고
    # 해당 숫자와 위치를 바꿔준다
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    # 그리고, inverse_point에 놓인 새로운 숫자를 기준으로
    # 그 이후의 숫자들을, 오름차순으로, 만들어준다 ( 그래야 다음 크기의 순열이므로 )
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

# 이전 크기의 순열을 찾기
# 위 원리의 반대를 생각하면 된다
# 뒤에서 올수록 작아져야 하는데 큰 숫자 , 즉, inverse_point를 구한다


def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
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
a = input().split()
small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]


while True:
    # 만약, 찾앗다면 break해서 나가기
    if check(small, a):
        break
    #
    # 더이상 다음의 permutation이 존재하지 않는다면
    # 즉, 현재가 가장 큰 수열이라면
    # 질문 : 그런데 가장 큰 순열까지 왔는데 정답이 아니라는 거 아닌가?
    # 그러면...어떻게 해야 하지...? 그래도 답으로 출력한다고 ?
    if not next_permutation(small):
        break

while True:
    if check(big, a):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
