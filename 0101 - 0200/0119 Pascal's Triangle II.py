class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex,i) for i in range(rowIndex+1)]
