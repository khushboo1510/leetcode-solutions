"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums)):
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
            else:
                x += 1
