class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum([g2 := list(g),sum(t for c,t in g2)-max(t for c,t in g2)][1] for k,g in groupby(zip(colors,neededTime),key = lambda pair: pair[0]))
