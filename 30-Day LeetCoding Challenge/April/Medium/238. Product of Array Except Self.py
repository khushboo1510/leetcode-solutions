"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Note: Please solve it without division and in O(n).
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [1] * n
        productLeft = nums[0]
        productRight = nums[n - 1]
        n = n - 1
        
        for i in range(1, len(nums)):
            result[i] *= productLeft
            result[n - i] *=productRight
            productLeft *= nums[i]
            productRight *= nums[n - i]
        
        return result