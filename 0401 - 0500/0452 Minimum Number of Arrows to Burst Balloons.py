class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        end = inf

        for s,e in sorted(points):
            if s <= end:
                end = min(end,e)
            else:
                ans += 1
                end = e

        return ans+1
