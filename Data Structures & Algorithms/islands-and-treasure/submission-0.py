from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        que = deque()

        def addRoom(r, c):
            if (r<0 or r == rows) or (c<0 or c== cols) or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            que.append((r,c))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    que.append([row, col])
                    visit.add((row, col))
        
        dist = 0
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist+=1