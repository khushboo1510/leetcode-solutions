"""
https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = []
        fresh = 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])
        count = 0
        queue = []
        while rotten:
            index = rotten.pop(0)
            i, j = index[0], index[1]

            for di, dj in directions:
                if 0 <= (i + di) < rows and 0 <= (j + dj) < cols and grid[i + di][j + dj] == 1:
                    fresh -= 1
                    grid[i + di][j + dj] = 2
                    queue.append([i + di, j + dj])
            
            if not rotten and queue:
                count += 1
                rotten = queue
                queue = []
        
        if fresh == 0:
            return count
        return -1
        