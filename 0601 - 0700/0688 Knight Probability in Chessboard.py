class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        probs = [[0]*n for i in range(n)]
        probs[row][column] = 1

        for i in range(k):
            probs2 = [[0]*n for i in range(n)]

            for r in range(n):
                for c in range(n):
                    for r2,c2 in [[r+1,c+2],[r+1,c-2],[r-1,c+2],[r-1,c-2],[r+2,c+1],[r+2,c-1],[r-2,c+1],[r-2,c-1]]:
                        if r2 in range(n) and c2 in range(n):
                            probs2[r2][c2] += probs[r][c]/8

            probs = probs2

        return sum(map(sum,probs))
