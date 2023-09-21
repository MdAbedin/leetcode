class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1

        for p1,p2 in combinations(points,2):
            slope = None if p2[0] == p1[0] else (p2[1]-p1[1])/(p2[0]-p1[0])
            ans = max(ans,2+sum(slope == (None if p[0] == p1[0] else (p[1]-p1[1])/(p[0]-p1[0])) for p in points if p not in [p1,p2]))

        return ans
