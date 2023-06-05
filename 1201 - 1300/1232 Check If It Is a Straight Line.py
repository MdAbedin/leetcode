class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return len({None if x1==x2 else (y2-y1)/(x2-x1) for (x1,y1),(x2,y2) in pairwise(coordinates)}) == 1
