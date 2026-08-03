from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        queue = deque()
        time, fresh = 0,0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for x, y in directions:
                    r, c = x+row, y+ col
                    if not valid(r, c) or grid[r][c] != 1:
                        continue 
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1



                


        