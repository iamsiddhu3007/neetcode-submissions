class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        validDirections = [(1,0),(-1,0), (0,1), (0,-1)]
        def dfs(row, col):
            if (row < 0 or col < 0 or row == rows or col == cols or board[row][col]!= 'O'):
                return
            board[row][col] = 'T'
            for x,y in validDirections:
                nextRow, nextCol = row + x, col + y
                dfs(nextRow, nextCol)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols -1]):
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        