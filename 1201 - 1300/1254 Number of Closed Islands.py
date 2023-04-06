class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:

        R,C = len(grid),len(grid[0])

        seen = set()

        ans = 0

        

        for r in range(R):

            for c in range(C):

                if (r,c) in seen or grid[r][c] == 1: continue

                    

                seen.add((r,c))

                dfs = [[r,c]]

                closed = True

                

                while dfs:

                    cr,cc = dfs.pop()

                    

                    for r2,c2 in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:

                        if r2 not in range(R) or c2 not in range(C):

                            closed = False

                        else:

                            if (r2,c2) not in seen and grid[r2][c2] == 0:

                                seen.add((r2,c2))

                                dfs.append([r2,c2])

                                

                if closed: ans += 1

                    

        return ans
