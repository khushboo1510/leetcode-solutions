# https://leetcode.com/problems/single-number-ii/

# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?    

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x, y = 0, 0 
        for num in nums:
            x = (x ^ num) & ~y
            y = (y ^ num) & ~x
            print(num,x,y)
        return x