class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = bisect_right(range(len(matrix)),target,key = lambda r: matrix[r][0])-1
        if r < 0: return False

        c = bisect_left(matrix[r],target)
        return c < len(matrix[0]) and matrix[r][c] == target
