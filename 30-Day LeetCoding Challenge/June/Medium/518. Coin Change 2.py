"""
https://leetcode.com/problems/coin-change-2/

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0 for j in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]