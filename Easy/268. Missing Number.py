"""
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i and nums[i] < n:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
       