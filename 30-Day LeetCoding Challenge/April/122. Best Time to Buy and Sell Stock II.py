"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = 0
        sell = 0
        cp = 0
        for i in range(len(prices)):
            
            if i == len(prices) - 1:
                if buy == 1 and cp < prices[i]:
                    profit += (prices[i] - cp)
                continue
                
            if buy == 0 and prices[i] < prices[i + 1]:
                cp = prices[i]
                buy = 1
                continue
            
            if buy == 1 and prices[i] > prices[i + 1]:
                profit += (prices[i] - cp)
                buy = 0

        return profit 
                