class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)

        for v1,v2 in edges:
            g[v1].add(v2)
            g[v2].add(v1)

        seen = set()
        ans = 0

        for v in range(n):
            if v in seen: continue

            seen.add(v)
            bfs = [v]

            for v2 in bfs:
                for v3 in g[v2]:
                    if v3 in seen: continue

                    seen.add(v3)
                    bfs.append(v3)

            ans += all(v2 in g[v1] for v1,v2 in combinations(bfs,2))

        return ans
