"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        num1 = -1
        for i,num in enumerate(nums):
            if num == 1:
                if num1 != -1:
                     if i - num1 <= k:
                        return False
                num1 = i
                   
        return True