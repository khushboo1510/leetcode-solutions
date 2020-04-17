"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        if not s:
            return True
        
        pStack = []
        starStack = []
        i = 0
        for ch in s:
            if ch == '(':
                pStack.append(i)
            if ch == '*':
                starStack.append(i)
            if ch == ')':
                if pStack:
                    pStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            i += 1
        
        while pStack and starStack:
            if pStack.pop() > starStack.pop():
                return False
        return not pStack
        