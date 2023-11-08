class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return t >= max(abs(fx-sx),abs(fy-sy)) and not (t == 1 and (sx,sy) == (fx,fy))
