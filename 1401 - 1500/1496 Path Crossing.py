class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0,0)}
        x,y = 0,0

        for c in path:
            if c == "N": y += 1
            if c == "S": y -= 1
            if c == "E": x += 1
            if c == "W": x -= 1
            if (x,y) in seen: return True
            seen.add((x,y))

        return False
