"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Similar to Two Sum
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        d = {0 : 1}
        result = 0
        total = 0
        
        for num in nums:
            total += num
            
            if d.get(total - k):
                result += d.get(total - k)
            
            d[total] = d.get(total,0)+1
            
        return result