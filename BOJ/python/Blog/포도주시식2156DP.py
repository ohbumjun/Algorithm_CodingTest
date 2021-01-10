# https://www.acmicpc.net/problem/2156
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


if __name__ == "__main__" :

    n   = int(input())
    dy  = [0] * ( n + 3 )
    arr = [0] * ( n + 3 )
    
    for i in range(3, n + 3 ):
        # point : n + 3 까지 배열을 잡는 것.
        # 0 1, 2, 번째 모두 입력배열에 따라 값이 달라질 수 있기 때문이
        arr[i] = int(input())

    for i in range( 3 , n + 3 ) :
        # i-2번째 잔을 안마신 경우 > i, i-1 , i-3 번째 잔 마심 : arr[i] + arr[i-1] + dy[i-3]
        # i-1번째 잔을 안마신 경우 > i-1 번째 제외 i, + dy[i-2]까지  : arr[i] + dy[i-2]
        # i-1,i-2번째 잔을 모두 마신 경우 > i번째 잔 마시면 안됨 : dy[i-1]
        dy[i] = max(arr[i] + arr[i-1] + dy[i-3] , arr[i] + dy[i-2], dy[i-1])

    print(dy[-1])
        

    
    

    
