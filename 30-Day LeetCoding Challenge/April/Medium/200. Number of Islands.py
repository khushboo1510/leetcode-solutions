"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        islands = 0
        i = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in grid:
            while "1" in row:
                j = row.index("1")
                islands += self.findIsland(i, j, rows, cols, grid)
            i += 1
        return islands
            
    def findIsland(self, i: int, j: int, rows: int, cols: int, grid: List[List[str]]) -> int:
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0
        if grid[i][j] != "1":
                return 1
            
        grid[i][j] = "2"
        self.findIsland(i + 1, j, rows, cols, grid)
        self.findIsland(i - 1, j, rows, cols, grid)
        self.findIsland(i, j + 1, rows, cols, grid)
        self.findIsland(i, j - 1, rows, cols, grid)
        
        return 1
        
        