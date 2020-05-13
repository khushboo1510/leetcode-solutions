"""
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        nums = list(map(int, num))
        stack = []

        for x in nums:
            while k and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        s = ''.join(map(str, stack))
        return s.lstrip("0") if s and int(s) > 0 else "0"