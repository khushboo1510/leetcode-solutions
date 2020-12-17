# https://leetcode.com/problems/squares-of-a-sorted-array/
    
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.    

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = nums[0]
        for i in range(n):
            nums[i] = nums[i] * nums[i]
            
        if s >= 0:
            return nums
        result = [0 for _ in range(n)]
        start, end, x  = 0, n - 1, n - 1
        
        while start <= end:
            if nums[start] < nums[end]:
                result[x] = nums[end]
                end -= 1
            else:
                result[x] = nums[start]
                start += 1
                
            x -= 1
        return result
                
