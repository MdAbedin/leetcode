class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)

        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        bfs = [source]
        seen = {source}

        for v in bfs:
            if v == destination: return True
            
            for v2 in g[v]:
                if v2 in seen: continue
                seen.add(v2)
                bfs.append(v2)

        return False
