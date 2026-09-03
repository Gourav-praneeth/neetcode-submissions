class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0] * rows for _ in range(cols)]

        # for i in range(cols):
        #     row = []
        #     for j in range(rows):
        #         row.append(0)
        #     result.append(row)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result