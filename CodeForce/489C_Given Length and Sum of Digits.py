# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

m , n = map(int, input().split())

if n == 0 :
    if m ==1 :
        print("0 0")
    else:
        print("-1 -1")
else:
    # max 값 구함
    maxArr = [9] * ( m )
    for i in range(m):
        maxArr[i] = min(maxArr[i], n)
        n -= maxArr[i]
    
    # 만약 n이 m 다 넣었어도 남는다 > 오류
    print("maxArr", maxArr)
    if n > 0 :
        print("-1 -1")
    

    else:
        # min 값 뒤집음
        minArr = []
        for i in range(m):
            minArr.insert(0,maxArr[i])
            
        lt = 0
        
        # 0 여부 검사
        # 보이면, 맨 앞자리 -1, 해당 위치 + 1
        while minArr[lt] == 0 :
                lt += 1
                
        if lt > 0 and lt < m :
            minArr[0]  += 1
            minArr[lt] -= 1

        # print
        print( ''.join(map(str,minArr)) , ''.join(map(str,maxArr)) )
