"""
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        pos, left, right  = 0, 0, n-1
        
        while pos <= right:
            num = nums[pos]
            if num == 0:
                nums[pos] = nums[left]
                nums[left] = 0
                left += 1
                pos += 1
            elif num == 2:
                nums[pos] = nums[right]
                nums[right] = 2
                right -= 1
            else:
                pos += 1
        """
        Another Solution
        n = len(nums)
        i = 0
        
        for x in range(n):
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                continue
            elif nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
            i += 1
        """