class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0

        for i,time in enumerate(sorted(d/s for d,s in zip(dist,speed))):
            if time <= i: break
            ans += 1

        return ans
