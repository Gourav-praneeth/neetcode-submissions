class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # four directions to check for the island
        directions = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]
        # to track the islands
        count = 0

        rows = len(grid)    
        cols = len(grid[0])

        def dfs(r,c):  
            # boundary check of the matrix
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # if the pos is 0 then return since its notr an island
            if grid[r][c] == "0":
                return
            # mark the visited land as 0
            grid[r][c] = "0"

            # check for neighbors if its a land or water 
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)

        return count