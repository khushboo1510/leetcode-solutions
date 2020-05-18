"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d = defaultdict(int)
        for ch in s1:
            d[ch] += 1
        
        ns1 = len(s1)
        ns2 = len(s2)
        
        dummy = defaultdict(int)
        
        for i in range(ns2 - ns1 + 1):
            if not dummy:
                for j in range(i, i + ns1):
                    dummy[s2[j]] += 1
            else:
                if dummy[s2[i - 1]] == 1:
                    del dummy[s2[i - 1]]
                else:
                    dummy[s2[i - 1]] -= 1
                dummy[s2[i + ns1 - 1]] += 1
            if dummy == d:
                return True
        
        return False