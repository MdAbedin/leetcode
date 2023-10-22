class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        l = []
        
        for row in grid:
            p = 1
            row2 = []
            
            for num in row:
                p *= num
                p %= MOD
                row2.append(p)
                
            l.append(row2)
            
        ri = []
        
        for row in grid:
            p = 1
            row2 = []
            
            for num in row[::-1]:
                p *= num
                p %= MOD
                row2.append(p)
                
            ri.append(row2[::-1])
            
        u = []
        p = 1
        
        for row in l:
            p *= row[-1]
            p %= MOD
            u.append(p)
            
        d = []
        p = 1
        
        for row in l[::-1]:
            p *= row[-1]
            p %= MOD
            d.append(p)
            
        d.reverse()
        
        return [[(u[r-1] if r-1 >= 0 else 1)*(d[r+1] if r+1 < len(grid) else 1)*(l[r][c-1] if c-1 >= 0 else 1)*(ri[r][c+1] if c+1 < len(grid[0]) else 1)%MOD for c in range(len(grid[0]))] for r in range(len(grid))]
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
