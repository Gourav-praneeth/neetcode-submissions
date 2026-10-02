from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]
        
        queue = deque([])
        minutes = 0
        fresh_oranges = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append([nr,nc])
                            fresh_oranges -= 1
            minutes += 1

        if fresh_oranges > 0:
            return -1

        return minutes
