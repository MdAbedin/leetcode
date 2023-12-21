class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(x2-x1 for (x1,y1),(x2,y2) in pairwise(sorted(points)))
