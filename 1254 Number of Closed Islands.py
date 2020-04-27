class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    bfs = deque([[y,x]])
                    grid[y][x] = -1
                    is_closed = True
                    
                    while bfs:
                        cur_y, cur_x = bfs.popleft()
                        
                        for dy, dx in [[0,1],[1,0],[0,-1],[-1,0]]:
                            new_y, new_x = cur_y+dy, cur_x+dx
                            
                            if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
                                is_closed = False
                            else:
                                if grid[new_y][new_x] == 0:
                                    grid[new_y][new_x] = -1
                                    bfs.append([new_y, new_x])
                            
                    ans += 1 if is_closed else 0
                
        return ans
