# https://www.acmicpc.net/problem/2156
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


if __name__ == "__main__" :

    '''
    자. 여기서 중요한 것은, 현재 i 번째 포도주를 만났을 때
    무조건 그것을 시식해야 하는 것이 아니다 !!!

    보통 dp를 풀때, 그것을 무조건 시식하는 경우를 기준으로 dy[i]를 정의한다
    ex. dy[i]란, i번째 포도주를 마셨을 때 , 마실 수 있는 포도주 최대의 양 

    그러나 여기서는 다르게 정의한다
    dy[i] : i번째 포도주를 만났을 때, 마실수 있는 포도주 최대의 양 ( 꼭 안마셔도 된다. )

    
    '''

    n   = int(input())
    dy  = [0] * ( n + 3 )
    arr = [0] * ( n + 3 )
    
    for i in range(3, n + 3 ):
        # point : n + 3 까지 배열을 잡는 것.
        # 0 1, 2, 번째 모두 입력배열에 따라 값이 달라질 수 있기 때문이다
        # 또한, n이 3보다 작게 입력되는 경우가 있고, 이럴 때 if 이렇게 분기처리해주는 것보다, 이와 같이 idx를 넉넉하게 잡아 처리해주는 것이 필요하다
        arr[i] = int(input())

    for i in range( 3 , n + 3 ) :
        # i-2번째 잔을 안마신 경우 > i, i-1 , i-3 번째 잔 마심 : arr[i] + arr[i-1] + dy[i-3]
        # i-1번째 잔을 안마신 경우 > i-1 번째 제외 i, + dy[i-2]까지  : arr[i] + dy[i-2]
        # i-1,i-2번째 잔을 모두 마신 경우 > i번째 잔 마시면 안됨 : dy[i-1]
        dy[i] = max(arr[i] + arr[i-1] + dy[i-3] , arr[i] + dy[i-2], dy[i-1])

    print(dy[-1])
        

    
    

    
