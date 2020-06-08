"""
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log10(n) / math.log10(2)
        return x.is_integer()