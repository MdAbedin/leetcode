class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = defaultdict(list)
        for v1,v2 in edges: parents[v2].append(v1)

        def solve(v0):
            bfs = [v0]
            seen = {v0}

            for v in bfs:
                for p in parents[v]:
                    if p in seen: continue
                    seen.add(p)
                    bfs.append(p)

            return sorted(bfs[1:])

        return map(solve,range(n))
