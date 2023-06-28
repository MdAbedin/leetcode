class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for (i1,i2),p in zip(edges,succProb):
            g[i1].append([i2,p])
            g[i2].append([i1,p])

        pq = [[-1,start]]
        bests = defaultdict(lambda: -inf, {start: 1})

        while pq:
            p,i = heappop(pq)
            p = -p
            if p < bests[i]: continue
            if i == end: return p

            for i2,p2 in g[i]:
                if p*p2 > bests[i2]:
                    bests[i2] = p*p2
                    heappush(pq, [-p*p2,i2])

        return 0
