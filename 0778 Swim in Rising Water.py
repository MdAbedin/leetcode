class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        seen = set((0,0))
        frontier = [(0,0)]
        
        while True:
            new_frontier = []
            
            while frontier:
                y,x = frontier.pop()
                
                if grid[y][x] <= t:
                    if (y,x) == (len(grid)-1,len(grid)-1): return t
                    
                    for ny,nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
                        if 0<=ny<len(grid) and 0<=nx<len(grid) and (ny,nx) not in seen:
                            seen.add((ny,nx))
                            frontier.append((ny,nx))
                else:
                    new_frontier.append((y,x))
        
            frontier = new_frontier
            t += 1
