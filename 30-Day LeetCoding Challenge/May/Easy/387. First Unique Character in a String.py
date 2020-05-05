"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        index = {}
        for i, ch in enumerate(s):
            d[ch] = d.get(ch, 0) + 1
            index[ch] = i

        for key, value in d.items():
            if value == 1:
                return index[key]
            
        return -1