'''
참조 풀이 : https://www.youtube.com/watch?v=Qf5R-uYQRPk
문제 : https://www.acmicpc.net/problem/9251

1) Top_Bottom
abcde
ace

의 LCS는
ace 다.

어떻게 하여 ace가 되는 것일까?

동적게획법을 사용하며
Top > Bottom 방식을 사용한다.

LCS( P0, Q0 ) 라는 함수를 사용한다고 해보자 //

2가지 경우로 나눌 수 있다

1) Case 1 : 두 문자열의 끝이 같은 경우
P0 = '[P1] x'
Q0 = '[Q1] x'

 이 경우는, 맨 마지막 문자열 앞까지의 LCS + 1이다
즉, LCS( P0, Q0) = 1 + LCS(P1, Q1)

2) Case 2 : 두 문자열의 끝이 다른 경우

P0 = '[P1]  x'
Q0 = '[Q1]  y'

이 경우, 2가지를 고려한다

> P 문자열의 끝 x를 제외 , LCS( P1, Q)
> Q 문자열의 끝 y를 제외 , LCS( P, Q1)

즉, LCS(P0, Q0) = max( LCS(P1, Q) , LCS(P, Q1) )


그리고 Memoization을 추가로 활용한다면
아래와 같은 코드 구조가 나온다

// Initializa arr[n][m] to undefined
def LCS( P, Q, n, m) : // n, m : num of strings from beginnig

    if arr[n][m] != undefined : return arr[n][m]

    // 맨끝에서 결국 맨 앞까지 와서, 빈 str 끼리 비교할 경우
    if n == 0  or m == 0 :
        result = 0

    // 끝의 문자열이 동일할 경우
    else if P[n-1] == Q[m-1] : 
        result = 1 + LCS(P,Q, n-1, m-1)
    // 끝의 문자열이 다를 경우
    else if P[n-1] != Q[n-2] :
        tmp1 = LCS(P, Q, n-1, m)
        tmp2 = LCS(P, Q, n, m-1)
        result = max(tmp1, tmp2)
    
    arr[n][m] = result

    return result


'''
# 1) Top Bottom
# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


def LCS( P, Q, n, m) : # n, m : num of strings from beginnig
    global result

    if arr[m][n] != 0 : return arr[m][n]

    # 맨끝에서 결국 맨 앞까지 와서, 빈 str 끼리 비교할 경우
    if n == 0  or m == 0 :
        result = 0

    # 끝의 문자열이 동일할 경우
    elif P[n-1] == Q[m-1] : 
        result = 1 + LCS(P,Q, n-1, m-1)
    # 끝의 문자열이 다를 경우
    elif P[n-1] != Q[m-1] :
        tmp1 = LCS(P, Q, n-1, m)
        tmp2 = LCS(P, Q, n, m-1)
        result = max(tmp1, tmp2)
    
    arr[m][n] = result

    return result

if __name__ == "__main__" :

    aArr = list(input())
    bArr = list(input())

    n = len(aArr)
    m = len(bArr)

    # 공집합 표현을 위해 인덱스가 한줄씩 추가 ( 0번째행과 0번째 열은, 공집합 의미 ) 
    arr = [[0] * (n+1) for _ in range(m + 1)]
    result = 0

    # n, m :문자열의 길이
    print(LCS(aArr, bArr, n, m))
    


# 2) Bottom_Top
if __name__ == "__main__" :

    aArr = list(input())
    bArr = list(input())

    n = len(aArr)
    m = len(bArr)

    # 공집합 표현을 위해 인덱스가 한줄씩 추가 ( 0번째행과 0번째 열은, 공집합 의미 ) 
    dp = [[0 for _ in range( n + 1 )] for _ in range( m + 1 )]

    # 첫번째 arr, aArr 이 열
    # 두번째 arr, bArr 이 행

    for x in range( 1, len(bArr) + 1 ) :
        for y in range(1, len(aArr) + 1 ):
            if aArr[y-1] == bArr[x-1] :
                dp[x][y] = dp[x-1][y-1] + 1
            else:
                dp[x][y] = max( dp[x-1][y], dp[x][y-1] )

    print(dp[-1][-1])
            

    

    

    
    




