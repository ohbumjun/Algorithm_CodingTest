# https://leetcode.com/problems/coin-change/submissions/

class Solution:
    def __init__(self):
        self.mem = {0: 0}
        self.coins = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        result = self.minCoin(amount)
        if result == int(1e9):
            return -1
        else:
            return result

    def minCoin(self, money):
        minN = int(1e9)
        # 최소값을 구하는 문제 --> recursive 과정에서 money가 minus가 되면 maxint를 리턴해줘서,
        # 유효하게 count 처리 되는 것을 방지한다
        if money < 0:
            return minN
        if money in self.mem:
            return self.mem[money]
        for coin in self.coins:
            if coin > money:
                continue
            minN = min(minN, self.minCoin(money - coin) + 1)
        self.mem[money] = minN
        return minN
