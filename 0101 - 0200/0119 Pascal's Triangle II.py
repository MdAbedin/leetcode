class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return map(partial(comb,rowIndex),range(rowIndex+1))
