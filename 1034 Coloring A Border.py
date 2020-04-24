class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        
        bfs = deque([(r0,c0)])
        visited = {(r0,c0)}
        
        while bfs:
            y, x = bfs.popleft()
            is_border = False

            for y_shift, x_shift in [[0,1],[1,0],[0,-1],[-1,0]]:
                new_y, new_x = y+y_shift, x+x_shift
                
                if new_y >= 0 and new_y < len(grid) and new_x >= 0 and new_x < len(grid[0]) and grid[new_y][new_x] == grid[y][x] and (new_y, new_x) not in visited:
                    bfs.append((new_y, new_x))
                    visited.add((new_y, new_x))

                if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]) or (grid[new_y][new_x] != 'border' and grid[new_y][new_x] != grid[y][x]):
                    is_border = True
                    
            if is_border: grid[y][x] = 'border'
                
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'border':
                    grid[y][x] = color
                    
        return grid
