class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        cols = len(grid[0])
        print(cols)
        
        for row in grid:
            for j in range(cols - 1, -1, -1):
                if row[j] >= 0:
                    break
                count += 1
        
        return count