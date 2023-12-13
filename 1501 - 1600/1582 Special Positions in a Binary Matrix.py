class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(mat[r][c] == 1 and sum(mat[r])+sum(mat[r2][c] for r2 in range(len(mat))) == 2 for r in range(len(mat)) for c in range(len(mat[0])))
