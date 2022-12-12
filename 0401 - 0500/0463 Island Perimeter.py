class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for y in range(len(grid)):
          for x in range(len(grid[0])):
            if grid[y][x] == 1:
              ans += 4
              
              for dy, dx in [[1,0], [0,1], [-1,0], [0,-1]]:
                ny, nx = y+dy, x+dx

                if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]) and grid[ny][nx] == 1:
                  ans -= 1
                
        return ans
