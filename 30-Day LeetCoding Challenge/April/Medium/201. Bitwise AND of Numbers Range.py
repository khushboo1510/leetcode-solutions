"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0 or m == n:
            return m
        
        if len(bin(m)) != len(bin(n)):
            return 0
        
        mb = f"{m:#033b}"
        nb = f"{n:#033b}"
        result = 0

        while mb.find('1') == nb.find('1'):
            pos = mb.find('1')
            msb = 32 - pos
            msbint = pow(2, msb)

            result += msbint

            m = m - msbint
            n = n - msbint
            
            mb = f"{m:#033b}"
            nb = f"{n:#033b}"

        return result 