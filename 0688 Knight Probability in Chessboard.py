class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        grid = [[0]*(N+4) for i in range(N+4)]
        for y in range(2,2+N):
            for x in range(2,2+N):
                grid[y][x] = 1
            
        moves = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
        for i in range(K):
            cp = [[0]*(N+4) for i in range(N+4)]
            
            for y in range(2,2+N):
                for x in range(2,2+N):
                    for dy,dx in moves:
                        cp[y][x] += 1/8*grid[y+dy][x+dx]
                        
            grid = cp
                        
        return grid[2+r][2+c]
