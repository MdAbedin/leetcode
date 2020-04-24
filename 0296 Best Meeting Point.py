class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ans = 0
        num_homes = sum(sum(row) for row in grid)
        median_row = median_col = 0
        median_row_found = median_col_found = False
        home_num = -1
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                home_num += grid[y][x]
                
                if home_num == num_homes//2:
                    median_row = y
                    median_row_found = True
                    break
                    
            if median_row_found: break
        
        home_num = -1
        
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                home_num += grid[y][x]
                
                if home_num == num_homes//2:
                    median_col = x
                    median_col_found = True
                    break
                    
            if median_col_found: break
            
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                ans += grid[y][x] * (abs(median_row-y) + abs(median_col-x))
                
        return ans
