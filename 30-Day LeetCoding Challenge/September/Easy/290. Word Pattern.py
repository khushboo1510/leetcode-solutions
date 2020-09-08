# https://leetcode.com/problems/word-pattern/
    
# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        pattern_d = {}

        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False
        
        for i, ch in enumerate(pattern):
            if ch not in pattern_d:
                pattern_d[ch] = words[i]
            else:
                if pattern_d[ch] != words[i]:
                    return False
                
        return True