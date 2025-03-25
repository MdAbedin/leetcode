class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        for coords in [sorted([r[0],r[2]] for r in rectangles),sorted([r[1],r[3]] for r in rectangles)]:
            cuts = 0
            p = coords[0][1]

            for s,e in coords:
                if s >= p: cuts += 1
                p = max(p,e)

            if cuts >= 2: return True

        return False
