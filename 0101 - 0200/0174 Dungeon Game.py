class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R,C = len(dungeon),len(dungeon[0])
        
        @cache
        def solve(r,c):
            if r == R or c == C: return inf
            if (r,c) == (R-1,C-1): return max(1,1-dungeon[r][c])
            return max(1,min(solve(r+1,c),solve(r,c+1))-dungeon[r][c])

        return solve(0,0)
