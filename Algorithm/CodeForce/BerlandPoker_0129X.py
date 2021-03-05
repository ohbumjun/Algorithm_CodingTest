# https://codeforces.com/problemset/problem/1359/A


import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

'''
m <= n // k
res = m

m == 0
res = 0

m > n // k
res = ?

1) tmp = m // ( n // k )
k - tmp 가 답 

m > n // k and n == k
m = 0

'''

n   = int(input())
res = 0

for _ in range(n):
    
    T , J , P = map( int , input().split() )
    if J <= T // P :
        res = J
    elif J == 0:
        res = 0
    else: # J > T // P
        '''
        max1 : 제일 많은 조커를 가진 사람. 이 가진 조커
        max2 : 그 사람 외, 제일 많은 조커를 가진 사람. 이 가진 조커

        우리가 구하고자 하는 것은 max1 - max2 이다.

        그러면, T // P 는 곧 max1 이다.

        J > T // P 인 상태에서
        한 사람이 가질 수 있는 조커의 최대 수가 T // P 이기 때문이다.
        즉, T // P가 max1 인 것이다.

        이제, max2를 구해볼 것이다. 어떻게 ?
        P는 총 사람 수,
        이제 1명한테는 조커를 이미 나눠줬기 때문에 ( max1 )
        나머지 사람들에게 조커를 나눠준다고 생각해보자

        max2를 구해야 하는데, max2가 최소가 되어야 ,
        우리가 구하고자 하는
        max( max1 - max2 )를 구할 수 있다.

        그렇다면, max2를 최소화 하는 방법으로는,
        모든 사람들에게 최대한 균등하게 나눠주는 방법이다.

        즉, 현재 남은 조커 수는 J - tmp

        남은 사람 수는 P - 1

        따라서, 남은 사람, 한명이 가질 수 있는 조커의 개수는
        J - tmp // P - 1 이다.

        만약 J - tmp % P - 1 == 0 이라면,,
        즉, 모두가 균등하게 나눠갖게 된다면

        max2는 곧, J - tmp // P - 1 이다.

        하지만 !!!
        만일, J - tmp % P - 1 != 0 이라면,
        모두에게 균등하게 나눠주고도, 여전히 조커가 남아있는 상황이므로,

        그것을 또한 1개씩 추가로 나눠준다

        그러면 max2는 곧, J - tmp // P - 1  + 1 이 되는 것이다
         
        '''
        tmp  = T // P
        if J > tmp :
            if ( J - tmp ) % ( P - 1 ) == 0 :
                res = tmp - ( ( J - tmp ) // ( P - 1 )  )
            else :
                res = tmp - ( ( J - tmp ) // ( P - 1 ) + 1 )
            
        # 나누고

        # 나눈 몫보다, J가 크다면

        # J에서, 나눈 몫을 빼고

        # J - 몫. 을 기준으로 다시 보는데

        # P - 1 명으로 나누어떨어진다면

        # J - ( J - 몫 // P - 1 )

        # 만약, 나머지가 있다면

        # J - ( J - 몫 // P - 1 + 1) 

    print(res)

