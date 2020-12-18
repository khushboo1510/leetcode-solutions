# https://leetcode.com/problems/increasing-triplet-subsequence/
    
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')
        
        for num in nums:
            if j < num:
                return True
            if i < num:
                j = min(j, num)
            elif num < i:
                i = num
                
        return False
