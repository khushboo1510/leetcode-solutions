"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        if n == 2:
            return True
        
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        
        if x2 - x1 == 0:
            for i in range(3, n):
                x, y = coordinates[i][0], coordinates[i][1]
                if x != x1:
                    return False
            return True
        
        slope = (y2 - y1) / (x2 - x1)
        
        b = y2 - (slope * x2)
        
        for i in range(3, n):
            x, y = coordinates[i][0], coordinates[i][1]
            if y != (x * slope) + b:
                return False
            
        return True