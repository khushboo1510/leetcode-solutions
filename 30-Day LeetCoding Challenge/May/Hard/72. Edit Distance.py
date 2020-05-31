"""
https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        
        for i in range(len(dp[0])):
            dp[0][i] = i
        for i in range(len(dp)):
            dp[i][0] = i
            
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        
        return dp[-1][-1]