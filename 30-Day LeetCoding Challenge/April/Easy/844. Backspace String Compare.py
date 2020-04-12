"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stackS = []
        stackT = []
        
        for ch in S:
            if ch == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(ch)
                
        for ch in T:
            if ch == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(ch)
                
        return stackT == stackS            