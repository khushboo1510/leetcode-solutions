"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        return ' '.join(words)