class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(row,i) for i in range(row+1)] for row in range(numRows)]
