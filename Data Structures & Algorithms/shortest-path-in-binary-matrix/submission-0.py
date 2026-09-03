from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()

        directions = [
            (-1,1),
            (-1,0),
            (-1,-1),
            (0,1),
            (0,-1),
            (1,0),
            (1,1),
            (1,-1)
        ]

        if grid[0][0] == 1:
            return -1
                
        if grid[len(grid)-1][len(grid)-1] == 1:
            return -1

        distance = 1 

        queue.append((0,0))

        grid[0][0] = 1
               
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                        return distance
                
                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            queue.append((nr,nc))
            distance += 1
        return -1

                    


        