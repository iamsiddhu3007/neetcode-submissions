class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(x,y):
            return 0<= x < len(grid) and 0<=y<len(grid[0]) and grid[x][y] == '1'
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()

        def dfs(row, col):
            for x, y in directions:
                nextRow, nextCol = row+x, col+y
                if valid(nextRow, nextCol) and valid(row, col) and (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    dfs(nextRow, nextCol)
        
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in seen and grid[x][y] == '1':
                    ans+=1
                    seen.add((x,y))
                    dfs(x, y)
        return ans
        