"""
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = ['#']
        
        pairs = { ')':'(', '}':'{',']':'['}
        
        for ch in s:
            if ch in pairs and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 1