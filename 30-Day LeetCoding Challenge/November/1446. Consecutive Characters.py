# https://leetcode.com/problems/consecutive-characters/
    
# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

class Solution:
    def maxPower(self, s: str) -> int:
        
        power, substring, count = 1, s[0], 1
        for ch in s[1:]:
            if ch == substring[-1]:
                count += 1
            else:
                power = max(power, count)
                count, substring = 1, ch
        
        return max(count, power)
