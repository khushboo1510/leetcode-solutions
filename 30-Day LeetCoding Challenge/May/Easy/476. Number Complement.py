"""
https://leetcode.com/problems/number-complement/

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""
class Solution:
    def findComplement(self, num: int) -> int:
        
        num = bin(num)[2:]
        s = '0b'
        
        for c in num:
            s += '1' if c == '0' else '0'
        
        return int(s, 2)