class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        seen = set()
        ans = 0
        
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 0 or (r,c) in seen:
                    continue
                    
                seen.add((r,c))
                dfs = [[r,c]]
                works = True
                
                while dfs:
                    cr,cc = dfs.pop()
                    
                    if grid1[cr][cc] == 0:
                        works = False
                        
                    for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                        if 0<=nr<len(grid2) and 0<=nc<len(grid2[0]) and grid2[nr][nc] == 1 and (nr,nc) not in seen:
                            seen.add((nr,nc))
                            dfs.append([nr,nc])
                            
                if works:
                    ans += 1
                        
        return ans
