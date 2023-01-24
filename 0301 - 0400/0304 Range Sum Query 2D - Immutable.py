class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.psums = matrix
        
        for r in range(len(self.psums)):
            for c in range(len(self.psums[0])):
                if r-1 >= 0: self.psums[r][c] += self.psums[r-1][c]
                if c-1 >= 0: self.psums[r][c] += self.psums[r][c-1]
                if r-1 >= 0 and c-1 >= 0: self.psums[r][c] -= self.psums[r-1][c-1]
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.psums[row2][col2]
        
        if row1-1 >= 0: ans -= self.psums[row1-1][col2]
        if col1-1 >= 0: ans -= self.psums[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0: ans += self.psums[row1-1][col1-1]
            
        return ans
