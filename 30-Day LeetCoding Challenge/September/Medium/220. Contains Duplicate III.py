# https://leetcode.com/problems/contains-duplicate-iii/
    
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
       
        n = len(nums)
        
        if t == 0 and n == len(set(nums)):
            return False
        
        for i in range(n):
            j = i + 1
            while j < n and j < i + k + 1:
                if abs(nums[i] - nums[j]) <= t:
                    return True
                j += 1
                
        return False