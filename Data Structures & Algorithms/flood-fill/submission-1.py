class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        Given - sr, sc as the starting point of the matrix
        we need top change the color of image[sr,sc]

        '''

        original_color = image[sr][sc] 

        # return the matrix if the starting pos is the color
        if original_color == color:
            return image

        directions = [
            (0,1), # up
            (1,0), # right
            (0, -1), # left
            (-1,0) # down
        ]

        def dfs(r, c):
            image[r][c] = color

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                    if image[nr][nc] == original_color:
                        dfs(nr,nc)
        dfs(sr, sc)
        return image