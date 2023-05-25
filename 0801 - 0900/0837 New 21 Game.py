class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0: return 1

        p = [1]+[0]*n
        s = 1

        for points in range(1,n+1):
            p[points] = s/maxPts
            if points < k: s += p[points]
            if 0 <= points-maxPts < k: s -= p[points-maxPts]

        return sum(p[k:])
