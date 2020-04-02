class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0:
                        count += 1
                    elif grid[i - 1][j] == 0:
                        count += 1
                    if i == m - 1:
                        count += 1
                    if j == 0:
                        count += 1
                    elif grid[i][j - 1] == 0:
                        count += 1
                    if j == n - 1:
                        count += 1
                else:
                    if j != 0 and grid[i][j - 1] == 1:
                        count += 1
                    if i != 0 and grid[i - 1][j] == 1:
                        count += 1
                    
        return count
                    
                    