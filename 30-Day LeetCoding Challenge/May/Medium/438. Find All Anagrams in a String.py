"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res = []
        np = len(p)
        n = len(s)

        d = defaultdict(int)
        for ch in p:
            d[ch] += 1
        dummy = defaultdict(int)
        for i in range(n - len(p) + 1):
            index = i
            if not dummy:              
                for j in range(np):
                    dummy[s[index]] += 1
                    index += 1
            else:
                dummy[s[index - 1]] -= 1
                dummy[s[index + np - 1]] += 1
                
            flag = True
            for ch in d:
                if ch not in dummy or dummy[ch] != d[ch]:
                    flag = False
                    break
            if flag:
                res.append(i)
                
        return res