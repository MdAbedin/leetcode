class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = list(range(len(isConnected)))

        def union(a,b): parents[find(a)] = find(b)

        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]

        for i in range(len(isConnected)):
            for j,connected in enumerate(isConnected[i]):
                if connected: union(i,j)

        return len({find(i) for i in range(len(isConnected))})
