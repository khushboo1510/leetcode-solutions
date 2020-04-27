"""
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        maxx = 0
        
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)] 
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i - 1][j - 1] == '1' else 0
                
                maxx = dp[i][j] if dp[i][j] > maxx else maxx
        
        return maxx ** 2