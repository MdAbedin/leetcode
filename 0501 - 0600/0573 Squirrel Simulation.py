def mdist(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)
    
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        tot = 2*sum(mdist(tree[0], tree[1], nut[0], nut[1]) for nut in nuts)
        
        return tot + min(mdist(squirrel[0], squirrel[1], nut[0], nut[1])-mdist(tree[0], tree[1], nut[0], nut[1]) for nut in nuts)
