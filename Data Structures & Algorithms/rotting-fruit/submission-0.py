from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c)) # stores current co-ordinate
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr,nc))
            minutes += 1

        if fresh > 0:
            return -1
        return minutes




