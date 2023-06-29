class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return [["."*c + "Q" + "."*(n-c-1) for c in cols] for cols in permutations(range(n)) if len({r-c for r,c in enumerate(cols)}) == len({r-(n-1-c) for r,c in enumerate(cols)}) == n]
