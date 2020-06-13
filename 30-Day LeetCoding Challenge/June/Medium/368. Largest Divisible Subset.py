"""
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return nums
        
        nums.sort()
        d = defaultdict(list)
        result = []
        for num in nums:
            arr = []
            for key in d:
                if num % key == 0 and len(d[key]) > len(arr):
                    arr = [] + d[key]
            arr.append(num)
            d[num] = arr
        return d[sorted(d, key = lambda x : -len(d[x]))[0]]