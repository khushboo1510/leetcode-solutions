"""
https://leetcode.com/problems/01-matrix/

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if not matrix or not matrix[0]:
            return matrix
        
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        queue = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visited[i][j] = 1
                    if i > 0 and matrix[i - 1][j] == 1 and visited[i - 1][j] == 0:
                        queue.append([i - 1, j])
                        visited[i - 1][j] = 1
                            
                    if j > 0 and matrix[i][j - 1] == 1 and visited[i][j - 1] == 0:
                        queue.append([i, j - 1])
                        visited[i][j - 1] = 1
                else:
                    if (i > 0 and matrix[i - 1][j] == 0) or \
                        (j > 0 and matrix[i][j - 1] == 0):
                            queue.append([i, j])
                            visited[i][j] = 1
        
        while queue:
            i,j = queue.pop(0)
            
            if i > 0 and visited[i - 1][j] == 0:
                visited[i - 1][j] = 1
                matrix[i - 1][j] += matrix[i][j]
                queue.append([i - 1,j])
                
            if i < rows - 1 and visited[i + 1][j] == 0:
                visited[i + 1][j] = 1
                matrix[i + 1][j] += matrix[i][j]
                queue.append([i + 1,j])
                
            if j > 0 and visited[i][j - 1] == 0:
                visited[i][j - 1] = 1
                matrix[i][j - 1] += matrix[i][j]
                queue.append([i,j - 1])
            
            if j < cols - 1 and visited[i][j + 1] == 0:
                visited[i][j + 1] = 1
                matrix[i][j + 1] += matrix[i][j]
                queue.append([i,j + 1])
                
        return matrix