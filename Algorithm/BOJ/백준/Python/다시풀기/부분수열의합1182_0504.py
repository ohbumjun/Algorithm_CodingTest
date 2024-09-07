# 부분수열의 합 https://www.acmicpc.net/problem/1182

'''
일반적인 투포인터 문제는 아닌듯 하다.

'크기가 양수인 부분수열 중에서'
라는 조건을 고려해야 하기 때문이다.

일반적으로는
투포인터를 활용하여 구간합을 구해가며
1) 목표치와 같을 때
2) 목표치보다 작을 때
3) 목표치보다 클때

이 3경우에 대해 연산을 다르게 해가면서
진행을 해야하는데 .... 흠 ...

아니! 생각 자체가 틀렸다 !!

?? 
이건 꼭 연속적으로 이루어져야 하는 것은 아니다 !

즉, 내가 생각한 부분수열은
1 2 3 4 일때
1 2 3 과 같이, 연속적으로 붙어있어야 하는 것이었다.

하지만... 아니다 !!
1 3 4 와 같이
서로 떼어져 있어도, 
원래 수열에서의 순서만 유지된다면

부분수열로 인식될 수 있다.

즉, 이것은 브루트 포스 문제이면서 동시에 '조합' 문제이다.
다만 '순서'를 고려해야 하는 '조합' 문제인 것이다.

'''

from random import randrange, randint
import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
목표하는 합을 만드는 숫자 조합의 수는 1개일 수도 ...n개일 수도 있다.

1개 ~ n개 로 만들어지는 모든 조합들을 다 조사하고

그 조합들 중에서 조건을 만족시키는 경우를 발견하면

그때 ans += 1을 해준다

( 사실상 이중 for문 개념 ) 

'''

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(L, idx, c, res):
    global ans
    if L == c:
        if res == s:
            ans += 1
        return
    else:
        for i in range(idx, n):
            if select[i] == 0:
                select[i] = 1
                dfs(L+1, i, c, res + arr[i])
                select[i] = 0


for i in range(1, n+1):
    select = [0] * (n + 1)
    dfs(0, 0, i, 0)

print(ans)
