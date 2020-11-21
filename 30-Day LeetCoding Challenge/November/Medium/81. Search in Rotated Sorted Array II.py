# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target or nums[start] == target:
                return True
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            elif nums[start] < target < nums[mid]:
                end = mid - 1
            else:
                start += 1
        return False
