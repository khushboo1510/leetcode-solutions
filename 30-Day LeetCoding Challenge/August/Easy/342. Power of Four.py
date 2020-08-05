# https://leetcode.com/problems/power-of-four/
    
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        return log(num, 4).is_integer()