"""
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0 for i in range(n)] for j in range(n)]
        
        fr, lr, fc, lc = 0, n - 1, 0, n - 1
        
        count = 1
        while fr <= lr and fc <= lc:
            
            for c in range(fc, lc + 1):
                mat[fr][c] = count
                count += 1
            fr += 1    
            
            for r in range(fr, lr + 1):
                mat[r][lc] = count
                count += 1
            lc -= 1
            
            for c in range(lc, fc - 1, -1):
                mat[lr][c] = count
                count += 1
            lr -= 1
            
            for r in range(lr, fr - 1, -1):
                mat[r][fc] = count
                count += 1
            fc += 1
            
        return mat