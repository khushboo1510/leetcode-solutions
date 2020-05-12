"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
            else:
                res -= nums[i]
        return abs(res)
           
