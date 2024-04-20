class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        R,C = len(land),len(land[0])
        ans = []

        for r in range(R):
            for c in range(C):
                if land[r][c] != 1: continue

                bfs = [(r,c)]

                for r2,c2 in bfs:
                    for r3,c3 in [[r2+1,c2],[r2-1,c2],[r2,c2+1],[r2,c2-1]]:
                        if r3 not in range(R) or c3 not in range(C) or land[r3][c3] != 1: continue
                        land[r3][c3] = 2
                        bfs.append((r3,c3))

                ans.append([*min(bfs),*max(bfs)])

        return ans
