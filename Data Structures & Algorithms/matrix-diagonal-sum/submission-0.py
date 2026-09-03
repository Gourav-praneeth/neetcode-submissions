class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        res = 0
        for i in range(len(mat)):
                res += mat[i][i]
                res += mat[i][len(mat) - 1 - i]

        if len(mat) % 2 == 0:
            res -= 0
        else:
            res -= mat[len(mat) // 2][len(mat) // 2]
        return res

        