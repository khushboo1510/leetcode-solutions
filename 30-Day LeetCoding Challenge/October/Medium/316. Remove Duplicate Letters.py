# https://leetcode.com/problems/remove-duplicate-letters/
    
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        counter = Counter(s)
        visited, stack = set(), []
        
        for ch in s:
            if ch not in visited:
                while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                    visited.remove(stack.pop())
                visited.add(ch)
                stack.append(ch)
            counter[ch] -= 1
        return ''.join(stack)
