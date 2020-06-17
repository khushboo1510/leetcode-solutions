# https://leetcode.com/problems/surrounded-regions/
    
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, rows, cols):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if board[i][j] == 'O':
                board[i][j] = 'NA'
                dfs(i + 1, j, rows, cols)
                dfs(i, j + 1, rows, cols)
                dfs(i - 1, j, rows, cols)
                dfs(i, j - 1, rows, cols)
        
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0, rows, cols)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1, rows, cols)
                
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j, rows, cols)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 'NA':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'              