class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R,C = len(rowSum),len(colSum)
        ans = [[0]*C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                x = min(rowSum[r],colSum[c])
                ans[r][c] += x
                rowSum[r] -= x
                colSum[c] -= x

        return ans
