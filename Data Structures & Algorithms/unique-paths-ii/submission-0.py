class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * cols for _ in range(rows)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for r in range(rows):
            for c in range(cols):

                if r == 0 and c == 0:
                    continue
                
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r == 0:
                    dp[r][c] = dp[r][c-1]
                elif c == 0:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r][c-1] + dp[r-1][c]

        return dp[rows-1][cols-1]



        # # initialise the matrix
        # rows = len(obstacleGrid)
        # cols = len(obstacleGrid[0])
        # #matrix = [[0 for j in range(cols)] for i in range(rows)]
        

        # # mark thr first rows with ones
        # for r in range(rows):
        #     if obstacleGrid[r][0] == 1:
        #         obstacleGrid[r][0] = 0
        #         break
        #     else:
        #         obstacleGrid[r][0] = 1
                
        # # mark the first col with ones and if you see an obstacle which is 1 converet that to O 
        # for c in range(cols):
        #     if obstacleGrid[0][c] == 1:
        #         obstacleGrid[0][c] = 0
        #         break
        #     else:
        #         obstacleGrid[0][c] = 1

        # for r in range(1,rows):
        #     for c in range(1,cols):
        #         if obstacleGrid[r][c] == 1:
        #             obstacleGrid[r][c] = 0
        #         else:
        #             obstacleGrid[r][c] = (obstacleGrid[r-1][c] + obstacleGrid[r][c-1])
            
        # return obstacleGrid[rows-1][cols-1]