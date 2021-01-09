# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

def w( a, b, c) :
    # 아래의 두 if 문의 순서가 중요하다
    # 반드시 아래 순서로 해야 한다. ( <= 0 조건이 > 20 조건보다 먼저 고려되어야 한다)
    if a <= 0 or b <= 0 or c <= 0 :
       return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    
    if dp[a][b][c] != 0 :
        return dp[a][b][c]
    
    elif a < b and b < c :
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else :
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c] 

    
if __name__ == "__main__" :

    MAX = 21
    dp = [ [[0] * MAX for _ in range(MAX) ] for _ in range(MAX) ]
    
    while True :
        a , b, c = list(map(int,input().split()))
        if a == b == c == -1 :
            break
        print("w(%d, %d, %d) = %d" %( a, b, c , w ( a, b, c ) ) ) 
    
    
        
            
            
            
                
            
    
