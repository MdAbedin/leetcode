class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        x,y = 0,0
        dx,dy = 0,1
        obstacles = set(map(tuple,obstacles))

        for c in commands:
            if c == -2:
                dx,dy = -dy,dx
            elif c == -1:
                dx,dy = dy,-dx
            else:
                for _ in range(c):
                    x2,y2 = x+dx,y+dy
                    if (x2,y2) not in obstacles: x,y = x2,y2

            ans = max(ans,x**2+y**2)

        return ans
