"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cols = len(text1)
        rows = len(text2)
        
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] += dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[rows][cols]