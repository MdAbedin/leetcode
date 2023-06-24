class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @cache
        def solve(prev,x2,y2,z2):
            return max((2+solve("AA",x2-1,y2,z2)) if x2 > 0 and prev[-1] != "A" else 0,
                       (2+solve("BB",x2,y2-1,z2)) if y2 > 0 and prev[-1] != "B" else 0,
                       (2+solve("AB",x2,y2,z2-1)) if z2 > 0 and prev[-1] != "A" else 0)
        
        return solve(" ",x,y,z)
