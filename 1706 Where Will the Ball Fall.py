class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        
        for i in range(len(grid[0])):
            y,x = 0,i
            h = True
            works = True
            
            while y < len(grid):
                if h:
                    orig = grid[y][x]
                    
                    if grid[y][x] == 1:
                        x+=1
                    else:
                        x-=1
                        
                    if x == len(grid[0]) or x == -1:
                        ans.append(-1)
                        works = False
                        break
                        
                    if grid[y][x] != orig:
                        ans.append(-1)
                        works = False
                        break
                else:
                    y+=1
                
                h = not h
                
            if works: ans.append(x)
        return ans
