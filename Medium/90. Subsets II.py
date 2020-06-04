"""
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = [[]]
        d = {}
        
        for num in nums:
            dummy = []
            for a in arr:
                if a and tuple(a + [num]) not in d:
                    d[tuple(a + [num])] = 1
                    dummy.append(a + [num])
                elif num not in d:
                    d[num] = 1
                    dummy.append([num])
            arr.extend(dummy)
        return arr