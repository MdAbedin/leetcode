class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        ans = 0
        tot = len(grid)-1
        
        while grid:
            found = False
            for i in range(len(grid)):
                cur_tot = 0
                for j in range(len(grid[i])-1, -1, -1):
                    if grid[i][j] == 0: cur_tot += 1
                    else: break
                        
                if cur_tot >= tot:
                    ans += i
                    tot -= 1
                    found = True
                    del grid[i]
                    break
            if not found:
                return -1
        
        return ans
