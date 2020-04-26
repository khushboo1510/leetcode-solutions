"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
"""

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        count = 0
        mat = [[0 for i in range(m)] for j in range(n)] 
        
        for ri,ci in indices:
            
            for i in range(m):
                mat[ri][i] += 1
            for row in mat:
                row[ci] += 1
                
        for row in mat:
            for col in row:
                if col % 2 != 0:
                    count += 1
        
        return count