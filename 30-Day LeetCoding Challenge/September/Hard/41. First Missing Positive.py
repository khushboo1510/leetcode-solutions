# https://leetcode.com/problems/first-missing-positive/
    
# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, i = len(nums), 0

        while i < n:
            if 0 < nums[i] <= n and i != nums[i] - 1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
                i -= 1
            i += 1
        
        count = 1
        for i in range(n):
            if i != nums[i] - 1:
                return count
            count += 1
        return count
