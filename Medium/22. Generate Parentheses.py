"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n < 1:
            return [""]

        result = []
        def generatePairs(n, left, right, pair):
            if left == n and right == n:
                result.append(pair)
            
            else:
                if left < n:
                    generatePairs(n, left + 1, right, pair+'(')
                if left - right > 0:
                    generatePairs(n, left, right + 1, pair+')')
            
        generatePairs(n, 0, 0, "")
        return result
