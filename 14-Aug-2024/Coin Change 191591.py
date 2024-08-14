# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(ans):
            if ans < 0:
                return inf
            if ans == 0:
                return 0
            if ans in memo:
                return memo[ans]
            mini = inf
            for coin in coins:
                mini = min(mini, dp(ans - coin) + 1)
            memo[ans] = mini
            return mini
        
        res = dp(amount)
        if res != inf:
            return res
        
        return -1




