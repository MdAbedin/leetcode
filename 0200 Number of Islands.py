class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    ans += 1
                    
                    bfs = deque()
                    bfs.append((y,x))
                    
                    while bfs:
                        cur_y, cur_x = bfs.popleft()
                        
                        grid[cur_y][cur_x] = '-1'
                        
                        for y_shift, x_shift in ((1,0), (0,1), (-1,0), (0,-1)):
                            new_y = cur_y + y_shift
                            new_x = cur_x + x_shift
                            
                            if new_y >= 0 and new_y < len(grid) and new_x >= 0 and new_x < len(grid[0]) and grid[new_y][new_x] == '1':
                                grid[new_y][new_x] = '-1'
                                bfs.append((new_y, new_x))
                                
        return ans
