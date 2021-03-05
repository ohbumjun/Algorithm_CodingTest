# https://codeforces.com/problemset/problem/1337/B
# 첫번째 풀이 : 틀린 답 ----------------------------------------------
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
sys.setrecursionlimit(10000)

n = int(input())

for i in range(n) :
    hitP, V, L = map(int,input().split())
    flag= True

    while True :
        if hitP <= 0 :
            break
        elif V == 0 and L == 0 :
            if hitP > 0 :
                print("V, L , hitP", V, L, hitP )
                flag = False
            break
        elif hitP >= 40 and V > 0 :
            hitP = ( hitP // 2 ) + 10
            V -= 1
        elif hitP >= 40 and V == 0 :
            hitP -= 10
            L -= 1
        elif hitP < 40 and L > 0 :
            hitP -= 10
            L -= 1
        elif hitP < 40 and L == 0  :
            hitP = ( hitP // 2 ) + 10
            V -= 1
        if ( i == 6 ) :
            print("hitP, V L:", hitP, V, L )

    if flag ==  False :
        print("NO")
    else:
        print("YES")

'''
기본적으로, 풀이의 핵심은 다음과 같다
해당 숫자가 40보다 크거나 같을 경우,

x // 2 + 10을 하는 것이
x - 10
하는 것보다 작은 값이 나온다.

처음에는, 최대한 많은 hp를 깎아야 한다고 생각했으므로
어떤 구간에서, 어떤 방법이 dragon의 hp를 가장 많이
깎는지를 생각한 결과. 

40을 기준으로, 
만약 void 공격이 남아있다면 void로 공격하고
40보다 아래는 최대한
light로 공격하는 코드를 생각했다.

물론, 40이상인데도, void 공격횟수가 남아있지 않으면
light로 공격하는 경우의 수도 고려해야 한다.

하지만, 
아래와 같이 input이 들어올 경우
69117 21 2

hitP, V L: 36 9 2
hitP, V L: 26 9 1
hitP, V L: 16 9 0
hitP, V L: 18 8 0
hitP, V L: 19 7 0
hitP, V L: 19 6 0
hitP, V L: 19 5 0
hitP, V L: 19 4 0
hitP, V L: 19 3 0
hitP, V L: 19 2 0
hitP, V L: 19 1 0
hitP, V L: 19 0 0

이렇게 19에서 계속 머무는 것을 알 수 있다.

즉, 20이하에서는 void가 절대 적용되어서는 안되는 것이다.
왜냐하면, 위와 같이, 계속 cycle을 돌기 때문이다.


'''


# 2번째 풀이 ------------------------------------------------------

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
sys.setrecursionlimit(10000)

n = int(input())

while n > 0 :
    hitP , V, L = map(int,input().split())

    flag = 0

    '''
    20 까지, V 가 남아있다면
    계속 V로 공격

    '''
    while( ( hitP > 20 ) and ( V > 0 ) ) :
        hitP = hitP // 2 + 10
        V -= 1
    '''
    이제, 20보다 작아진다면, 혹은 더이상 V가 없다면
    이제는 무조건 L로 조진다 ! 
    '''

    while( ( hitP > 0 ) and ( L > 0 ) ) :
        hitP -= 10
        L -= 1
        if hitP <=  0 :
            flag = 1
            break
    if flag == 1 :
        print("YES")
    else:
        print("NO")        


'''
그래서 기준을 바꿨다.
20으로 !!

즉, 비록 20 위에서, void를 적용하면
light를 적용하는 것에 비해
주는 숫자의 크기는 작지만,

20아래에 왔을 때부터 light를 무조건 적용해야만
위와 같은 cycle이 돌지 않기 때문이다. 
'''