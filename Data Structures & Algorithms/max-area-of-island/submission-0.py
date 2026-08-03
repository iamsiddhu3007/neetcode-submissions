class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            return 0<= x< len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()

        def dfs(row, col):
            area = 1
            for x,y in directions:
                nextRow, nextCol = row+x, col+y
                if valid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    area += dfs(nextRow, nextCol)
            return area
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if valid(x,y) and (x,y) not in seen and grid[x][y] == 1:
                    seen.add((x,y))
                    curr_area = 1
                    max_area = max(max_area, dfs(x,y))
        return max_area
                    

                



        