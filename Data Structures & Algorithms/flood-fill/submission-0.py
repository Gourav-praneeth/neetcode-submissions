class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        
        def dfs(r,c):
            image[r][c] = color

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
            
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                    if image[nr][nc] == original:
                        dfs(nr,nc)
        
        dfs(sr,sc)
        return image

