# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


if __name__ == "__main__" :

    n     = int(input())
    dist = list(map(int,input().split()))
    costs  = list(map(int,input().split()))
    res   = 0

    # 첫번째 비용으로, 첫번째 거리는 무조건 가야 한다
    res  += ( costs[0] * dist[0] )

    minCost = costs[0]

    # 이제 2번째 도시부터,  for문을 돌면서, 최소 비용을 만나면, 해당 최소비용으로 만나는 거리들을 계속 곱해간다
    for i in range(1, len(costs)-1):
        if costs[i] < minCost :
            minCost = costs[i]

        res += minCost * dist[i]

    print(res)
        
    
    
    
    
    
        
        

    
    

    
