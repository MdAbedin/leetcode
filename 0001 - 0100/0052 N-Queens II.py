class Solution:
    def totalNQueens(self, n: int) -> int:
        return sum(len({r-c for r,c in enumerate(cols)}) == len({r-(n-1-c) for r,c in enumerate(cols)}) == n for cols in permutations(range(n)))
