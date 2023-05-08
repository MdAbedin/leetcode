class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:

        return sum(mat[i][i] for i in range(len(mat))) + sum(mat[i][~i] for i in range(len(mat))) - (mat[len(mat)//2][len(mat)//2] if len(mat)%2 == 1 else 0)
