# https://www.acmicpc.net/problem/10844

# 풀이 링크 :https://suri78.tistory.com/91



import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

'''

원리는 다음과 같다.
n 번째 자리 i 숫자는
n - 1번째 i - 1숫자 + n - 1번째 i + 1 숫자에서 오는 것이다.

dy [ n ] [ i ] = dy [ n -1 ][ i - 1 ] + dy[ n - 1 ][ i + 1 ]

다만, 0과 9의 경우는 예외.
0은 1에 서만 오기때문에
dy[ n ] [ 0 ] = dy [ n -1 ] [ 1 ]

9도 8에 서만 오기 때문에
dy[ n ] [ 9 ] = dy [ n -1 ] [ 8 ]


이와 같이 ,
2차원 배열을 선언해서, dp 방식으로 풀어도 된다.

그런데 1차원 배열로 압축해서 풀수 있다
stairs라는 dp 배열을 선언하고
stairs[i]는, i 숫자가, 제일 마지막 1의 자리수로 왔을 때,
그때 가능한, 계단 종류의 수. 로 정의한다.

즉, 3자리 숫자에 대한 경우의 수를 구한다면
먼저 처음 stairs는 다음과 같이 초기화 된다
[ 0 1 1 1 1 1 1 1 1 1  ]

그리고 for문은 2번을 돈다.
처음 for문은 2자리수를 고려할때,

ex. 1의 자리에 1이라는 숫자가 올 때는,
그 앞의 숫자가 0 혹은 1일 때 이다.

결국 tmp라는 배열은 선언하고
tmp = stairs[:]로 복사한다.

즉, 기존의 stairs 배열은 이제 , 한자리 앞의 숫자의 경우가 되는 것이다

ex.
stairs = [ 0 1 1 1 1 1 1 1 1 1  ] 였다면,, 이는 각숫자가 1의 자리로 올때 경우의 수 
tmp = [ 0 1 1 1 1 1 1 1 1 1  ] 이고, 이는 각 숫자가 , 10의 자리로 올때 경우의 수

그러면, 이제 stairs[i]는
tmp[ i - 1 ] + tmp [i + 1 ]이 되는 것이다.

왜 ? 1의 자릿수의 2가 올때는
10의 자릿수가 1일때와 3일때의 경우를 합친 것이기 때문이다.

단, stairs[0]은, tmp[1]일때만 가능
즉, 1의 자릿수가 0인 경우는, 10의 자릿수가 1일 때만 가능

같은 원리로 stairs[9] = tmp[8]

'''
n      = int(input())
stairs = [ 0, 1, 1, 1, 1, 1, 1, 1, 1 , 1]
mod    =  1000000000

for _ in range(n-1):
    tmp = stairs[:]
    stairs[0] = tmp[1] % mod
    for i in range( 1 , 9 ) :
        stairs[i] = ( tmp[i-1] + tmp[i+1] ) % mod
    stairs[9] = tmp[8]

print(sum(stairs) % mod)
    






'''
DFS 로 푸는 방법 : 시간 초과

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n   = int(input())
cnt = 0

def dfs(L,val,res):
    global cnt
    if L == n - 1 :
        cnt += 1
        return
    else:
        for x in [val -1, val + 1]:
            if x >= 0 and x < 10 :
                res.append(x)
                dfs( L + 1 , x ,res)
                res.pop()

for x in range( 1, 10 ):
    res = [x]
    dfs( 0 , x , res)

print(cnt % 1000000000)


'''

