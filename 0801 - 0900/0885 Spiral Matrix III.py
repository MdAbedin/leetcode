class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        seen = set()
        r,c = rStart,cStart
        dr,dc = -1,0
        ans = []

        while len(ans) < rows*cols:
            seen.add((r,c))
            if r in range(rows) and c in range(cols): ans.append((r,c))
            if (r+dc,c-dr) not in seen: dr,dc = dc,-dr
            r += dr
            c += dc

        return ans
