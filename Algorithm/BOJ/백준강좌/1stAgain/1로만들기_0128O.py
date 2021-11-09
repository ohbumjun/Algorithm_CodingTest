# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


if __name__ == "__main__" :

    '''
    동적 프로그래밍
    1부터 n까지의 올라가면서
    n을 1로 만들때의 최소 연산 횟수를 구해간다

    bottom-up 방식을 적용한다.
    '''
    n = int(input())
    f = [0] * ( n + 1 )

    f[1] = 0
    for i in range( 2, n + 1 ):
        f[i] = f[i-1] + 1

        # 2 곱하기 연산
        if i % 2 == 0 and f[i//2] + 1 < f[i] :
            f[i] = f[i//2] + 1
        # 3 곱하기 연산
        if i % 3 == 0 and f[i//3] + 1 < f[i] :
            f[i] = f[i//3] + 1

    print(f[n]) 
        


    '''
    dy[i]는 i라는 숫자를 1로 만드는 것 까지의 최소연산횟수.를 의미한다.

    f( n )은 다음과 같은 값 중에서 최소를 지닌다
    f( n - 1 ) + 1
    f( n // 2 )  + 1 : n //2 에서 2를 곱하는 것 = * 2 라는 연산으로 인해, 연산횟수 1 증가
    f( n // 3 )  + 1 : n //3 에서 3을 곱하는 것 = * 3 라는 연산으로 인해, 연산횟수 1 증가
    '''
        

        
        
        

        
        
    
    
    
    
    
        
        

    
    

    
