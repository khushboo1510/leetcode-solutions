"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        def binarySearch(row, low, high, target):
            if high <= low:
                return False
            
            mid = int((low+high) / 2)
            
            if row[mid] == target:
                return True
            if target < row[mid]:
                return binarySearch(row, low, mid, target)
            return binarySearch(row, mid + 1, high, target)
            
        for row in matrix:
            if row[-1] == target:
                return True
            elif row[-1] > target and binarySearch(row, 0, len(row), target):
                return True
        
        return False
    
                
            