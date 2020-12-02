# https://leetcode.com/problems/knight-probability-in-chessboard/
    
# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        DIRECTIONS = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        memo = {}
        def dfs(x, y, k, p):
            if (x, y, k) in memo:
                return memo[(x, y, k)]
            
            if not k:
                return p
            s = 0
            for dx, dy in DIRECTIONS:
                if 0 <= x + dx <= N - 1 and 0 <= y + dy <= N -1:
                    s += dfs(x + dx, y + dy, k - 1, p / 8) 
            
            memo[(x, y, k)] = s
            return memo[(x, y, k)]
        
        return dfs(r, c, K, 1)
