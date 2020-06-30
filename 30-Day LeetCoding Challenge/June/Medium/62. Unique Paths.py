# https://leetcode.com/problems/unique-paths/
    
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Constraints:
#     1 <= m, n <= 100
#     It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def findPaths(i, j):
            if i == n - 1 and j == m - 1:
                return 1
            
            if i >= n or j >= m:
                return 0
            
            if visited[i][j] > 0:
                return visited[i][j]

            res = findPaths(i + 1, j) + findPaths(i, j + 1)
            visited[i][j] = res
            return res
        
        visited = [[0 for j in range(m)] for i in range(n)]
        
        return findPaths(0, 0)