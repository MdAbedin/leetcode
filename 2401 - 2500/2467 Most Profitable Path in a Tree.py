class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = defaultdict(list)

        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        bfs = [0]
        prevs = {0:-1}

        for v in bfs:
            for v2 in g[v]:
                if v2 in prevs: continue

                prevs[v2] = v
                bfs.append(v2)

        bob_times = defaultdict(lambda:inf)
        t = 0

        while bob != -1:
            bob_times[bob] = t
            bob = prevs[bob]
            t += 1

        bfs = [[0,0,0,-1]]
        seen = {0}
        ans = -inf

        for v,s,t,p in bfs:
            s += 0 if bob_times[v] < t else (amount[v] if bob_times[v] > t else amount[v]//2)
            if g[v] == [p]: ans = max(ans,s)

            for v2 in g[v]:
                if v2 in seen: continue

                seen.add(v2)
                bfs.append([v2,s,t+1,v])

        return ans
