"""
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if not magazine and ransomNote:
            return False
        
        d = defaultdict(int)
        
        for c in magazine:
            d[c] += 1

        for r in ransomNote:
            if d[r] > 0:
                d[r] -= 1
            else:
                return False
        return True