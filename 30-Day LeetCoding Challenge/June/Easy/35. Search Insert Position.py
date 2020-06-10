"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        return bisect.bisect_left(nums, target)