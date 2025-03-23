class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9+7
        g = defaultdict(list)

        for v1,v2,t in roads:
            g[v1].append([v2,t])
            g[v2].append([v1,t])

        bests = defaultdict(lambda:[inf,-1],{0:[0,1]})
        pq = [[0,0]]

        while pq:
            t,v = heappop(pq)
            if t > bests[v][0]: continue

            for v2,t2 in g[v]:
                if t+t2 < bests[v2][0]:
                    bests[v2] = [t+t2,bests[v][1]]
                    heappush(pq,[t+t2,v2])
                elif t+t2 == bests[v2][0]:
                    bests[v2][1] += bests[v][1]
                    bests[v2][1] %= mod

        return bests[n-1][1]
