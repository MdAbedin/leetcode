class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R,C = len(isWater),len(isWater[0])
        bfs = [[r,c,0] for r in range(R) for c in range(C) if isWater[r][c]]
        ans = [[0 if isWater[r][c] else -1 for c in range(C)] for r in range(R)]

        for r,c,h in bfs:
            for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if r2 not in range(R) or c2 not in range(C) or ans[r2][c2] != -1: continue
                ans[r2][c2] = h+1
                bfs.append([r2,c2,h+1])

        return ans
