# https://leetcode.com/problems/valid-palindrome/
    
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.
    
# Constraints: s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = re.sub(r'[^a-zA-Z\d]', '', s).lower()
        
        return s == s[::-1]