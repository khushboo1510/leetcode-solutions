# https://leetcode.com/problems/maximum-product-subarray/
    
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        maxp = minp = nums[0]
        product = maxp
        
        for num in nums[1:]:
            if num < 0 :
                maxp, minp = minp, maxp
                
            maxp = max(num, maxp*num)
            minp = min(num, minp*num)
            
            product = max(product, maxp)

                
        return product