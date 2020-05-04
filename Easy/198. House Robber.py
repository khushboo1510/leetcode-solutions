"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the 
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0, 0] + nums
        n = len(nums)
        m = 0
        
        dp = [0 for i in range(n + 2)]
        for i in range(2, n):
            dp[i] = nums[i] + max(abs(nums[i - 1] - dp[i - 1]), dp[i - 2])
            
            m = dp[i] if dp[i] > m else m
                
        return m