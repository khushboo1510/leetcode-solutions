"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    
        for row in matrix:
            count += sum(row)
        return count