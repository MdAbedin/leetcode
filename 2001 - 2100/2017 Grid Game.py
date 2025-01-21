class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        s1,s2 = sum(grid[0]),0
        ans = inf

        for c in range(len(grid[0])):
            s1 -= grid[0][c]
            ans = min(ans,max(s1,s2))
            s2 += grid[1][c]

        return ans
