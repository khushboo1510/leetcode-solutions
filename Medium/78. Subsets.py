"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        arr = []
        for num in nums:
            arr.extend(result)
            for r in arr:
                if r:
                    result.append(r + [num])
                else:
                    result.append([num])
            arr = []
       
        return result