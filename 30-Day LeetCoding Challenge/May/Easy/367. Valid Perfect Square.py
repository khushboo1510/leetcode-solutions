"""
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l = 1
        r = (num // 2) + 1 
        while l <= r:
            mid = int((l + r)/ 2)
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False