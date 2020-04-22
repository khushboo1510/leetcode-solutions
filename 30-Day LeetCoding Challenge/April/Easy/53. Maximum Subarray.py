"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = -sys.maxsize - 1
        total = 0
        
        for num in nums:
            total += num
            result = max(result, total)
            total = max(total, 0)
        return result        
        