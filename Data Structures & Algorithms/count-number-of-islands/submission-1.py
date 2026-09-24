class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        directions = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            grid[r][c] = "0"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "1":
                        dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)

        return count

