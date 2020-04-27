import numpy

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        mat = numpy.array(matrix)
        
        def binarySearch(mat):
            print(mat)
            rows = len(mat)
            cols = len(mat[0])

            if rows <= 2 and cols <= 2:
                for i in range(rows):
                    for j in range(cols):
                        if mat[i][j] == target:
                            return True
                return False
            
            mid_row = int(rows / 2)
            mid_col = int(cols / 2)
            mid_val = mat[mid_row][mid_col]
            part1 = part2 = part3 = part4 = False
                
            if mid_val == target:
                return True
            
            if target < mid_val and binarySearch(mat[0:mid_row + 1, 0:mid_col+1]):
                return True
            else:
                if mat[0][mid_col] <= target <= mat[mid_row][cols - 1]:
                    if binarySearch(mat[:mid_row+1, mid_col:cols]):
                        return True
                    
                if mat[mid_row][0] <= target <= mat[rows-1][mid_col]:
                    if binarySearch(mat[mid_row:, :mid_col + 1]):
                        return True
                
                if mid_val <= target <= mat[rows - 1][cols - 1]:
                    if binarySearch(mat[mid_row:, mid_col:]):
                        return True
                
            return False
            
        return binarySearch(mat)