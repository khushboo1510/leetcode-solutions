"""
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        fr,lr,fc,lc = 0, rows - 1, 0, cols - 1
        result = []
        
        while fr <= lr and fc <= lc:
            for c in range(fc, lc + 1):
                result.append(matrix[fr][c])
                
            for r in range(fr + 1, lr + 1):
                result.append(matrix[r][lc])
            
            if fr != lr:   
                for c in range(lc - 1, fc - 1, -1):
                    result.append(matrix[lr][c])
            if fc != lc:
                for r in range(lr - 1, fr, -1):
                    result.append(matrix[r][fc])
                
            fr += 1
            lr -= 1
            fc += 1
            lc -= 1
        
        return result