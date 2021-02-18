# https://leetcode.com/problems/coin-change/

# 첫번째 풀이 : 일반적인 냅색 알고리즘
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dy = [amount + 1] * ( amount + 1)
        dy[0] = 0
        
        for coin in coins :
            for i in range( coin , amount + 1 ) :
                dy[i] = min( dy[i] , dy[i-coin] + 1 )
        
        if dy[-1] == amount + 1 :
            return -1
        else:
            return dy[-1]
        
'''
dy[j] : j원을 거슬러주는데 사용되는
최소한의 동전의 개수 
'''