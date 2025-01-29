class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for e in edges[::-1]:
            g = defaultdict(list)

            for v1,v2 in edges:
                if [v1,v2] == e: continue
                g[v1].append(v2)
                g[v2].append(v1)

            bfs = [1]
            seen = {1}

            for v in bfs:
                for v2 in g[v]:
                    if v2 in seen: continue
                    seen.add(v2)
                    bfs.append(v2)

            if len(bfs) == len(edges): return e
