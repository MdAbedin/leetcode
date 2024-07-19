class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [x for row in matrix for x,col in zip(row,zip(*matrix)) if [min(row),max(col)] == [x,x]]
