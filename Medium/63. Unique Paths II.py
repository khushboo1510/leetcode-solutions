"""
https://leetcode.com/problems/unique-paths-ii/submissions/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if not obstacleGrid and not obstacleGrid[0]:
            return 0
       
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1]:
            return 0
        
        obstacleGrid[0][0] = 1
        for i in range(1, rows):
            obstacleGrid[i][0] = obstacleGrid[i -1][0] if obstacleGrid[i][0] == 0 else 0
        for i in range(1, cols):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] if obstacleGrid[0][i] == 0 else 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                obstacleGrid[i][j] =  obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0
         
        return obstacleGrid[-1][-1]