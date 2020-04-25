"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        n = len(nums)
        
        maximum = 0
        
        for i in range(n):
            if i > maximum:
                return False
            if maximum >= n - 1:
                return True
            
            if i + nums[i] > maximum:
                maximum = i + nums[i]
        return False
                