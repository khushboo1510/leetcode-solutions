"""
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = []
        n = len(S)
        
        def findPermutations(substring, index):
            if index == n:
                result.append(substring)
                return
            if S[index].isalpha():
                findPermutations(substring + S[index].lower(), index + 1)
                findPermutations(substring + S[index].upper(), index + 1)
            else:
                findPermutations(substring + S[index], index + 1)
                
        findPermutations('', 0)
        return result