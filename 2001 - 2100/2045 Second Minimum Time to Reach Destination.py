class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = defaultdict(list)

        for v,v2 in edges:
            g[v].append(v2)
            g[v2].append(v)

        pq = [(0,1)]
        bests = defaultdict(lambda:inf,{1:0})
        bests2 = defaultdict(lambda:inf)

        while pq:
            t,v = heappop(pq)
            if t > bests2[v]: continue
            if (t//change)%2: t += change - t%change

            for v2 in g[v]:
                if t+time < bests[v2]:
                    bests[v2] = t+time
                    heappush(pq,(t+time,v2))
                elif bests[v2] < t+time < bests2[v2]:
                    if v2 == n: return t+time
                    bests2[v2] = t+time
                    heappush(pq,(t+time,v2))
