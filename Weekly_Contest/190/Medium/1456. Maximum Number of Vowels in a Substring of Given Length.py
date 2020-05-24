"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        ss = ""
        result = 0
        count = 0
        i = 0          
        while i < len(s):
            if ss:
                if ss[0] in vowels:
                    count -= 1
                if s[i] in vowels:
                    count += 1
                ss = ss[1:] + s[i]
            else:
                for j in range(k):
                    ss += s[j]
                    if s[j] in vowels:
                        count += 1
                    i += 1
                i -= 1
            i += 1
            result = max(result, count)
        return result