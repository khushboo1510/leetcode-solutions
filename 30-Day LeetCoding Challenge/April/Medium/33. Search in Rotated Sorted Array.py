"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

"""
Referred: https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return - 1
        
        n = len(nums)
        
        pivot = self.findPivot(nums, 0, n - 1)
        
        if nums[pivot] == target: 
            return pivot 
        if nums[0] <= target: 
            return self.binarySearch(nums, 0, pivot-1, target)
        return self.binarySearch(nums, pivot+1, n-1, target)
    
    def binarySearch(self, arr, low, high, target):
        
        if high < low:
            return -1
        
        mid = int((low + high) / 2)
        
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return self.binarySearch(arr, low, mid - 1, target)
        return self.binarySearch(arr, mid + 1, high, target)
    
    def findPivot(self, arr, low, high):
        
        if high < low:
            return -1
        if high == low:
            return low
        
        mid = int((low + high) / 2)
        
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if low < mid and arr[mid - 1] > arr[mid]:
            return mid - 1
        if arr[low] > arr[mid]:
            return self.findPivot(arr, low, mid - 1)
        return self.findPivot(arr, mid + 1, high)