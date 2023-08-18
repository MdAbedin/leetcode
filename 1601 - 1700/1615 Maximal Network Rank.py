class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(set)
        
        for a,b in roads:
            g[a].add(b)
            g[b].add(a)

        return max(len(g[i])+len(g[i2])-(i2 in g[i]) for i in range(n) for i2 in range(i+1,n))
