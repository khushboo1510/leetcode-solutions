# https://leetcode.com/problems/break-a-palindrome/
    
# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

# After doing so, return the final string.  If there is no way to do so, return the empty string.

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i, ch in enumerate(palindrome[:n//2]):
            if ch != 'a':
                return palindrome[: i] + 'a' + palindrome[i + 1 :]
        
        return palindrome[:-1] + 'b'
