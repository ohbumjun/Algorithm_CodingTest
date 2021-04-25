# https://leetcode.com/problems/coin-change/

# 첫번째 풀이 : 일반적인 냅색 알고리즘
# Python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dy = [amount + 1] * (amount + 1)
        dy[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dy[i] = min(dy[i], dy[i-coin] + 1)

        if dy[-1] == amount + 1:
            return -1
        else:
            return dy[-1]


'''
dy[j] : j원을 거슬러주는데 사용되는
최소한의 동전의 개수 
'''

# Javascript
'''
var coinChange = function(coins, amount) {
    /*
    > dp
    dp[i] : i개 coin을 나눠줄때의 최소 
    아니다. 전형적인 냅색 알고리즘이다
    1 고려, 2 고려, 5고려 하는 원리이다 
    */
    if(amount == 0) return 0
    let coinLen = coins.length
    let maxInt = Number.MAX_SAFE_INTEGER
    let dp = Array(amount + 1).fill(maxInt)
    dp[0] = 0
    for(let i = 0 ; i < coinLen; i++){
        for(let j = coins[i] ; j < amount+1; j++ ){
            dp[j] = Math.min(dp[j],dp[j-coins[i]] + 1)
        }
    }
    return dp[amount] == maxInt ? -1 : dp[amount] 
};
'''

# javascript
# recursive + memoization ( dp )
