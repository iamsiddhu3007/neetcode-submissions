class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(x,y):
            return 0<=x<len(board) and 0<=y<len(board[0])

        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if not valid(row,col) or word[i] != board[row][col] or (row, col) in path:
                return False
            path.add((row, col))
            
            res = (dfs(row + 1, col, i+1) or
                    dfs(row - 1, col, i+1) or
                    dfs(row, col + 1, i+1) or
                    dfs(row, col - 1, i+1))
            path.remove((row, col))
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
            




        