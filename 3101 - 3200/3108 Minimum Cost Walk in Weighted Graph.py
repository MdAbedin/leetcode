class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        
        for v1,v2,w in edges:
            g[v1].append([v2,w])
            g[v2].append([v1,w])
        
        parents = list(range(n))
        
        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        
        def union(x1,x2): parents[find(x1)] = find(x2)
            
        seen = set()
        ans = {}
        
        for v in range(n):
            if v in seen: continue

            seen.add(v)
            bfs = [v]
            ans2 = 2**17-1
            
            for v2 in bfs:
                for v3,w in g[v2]:
                    ans2 &= w
                    if v3 in seen: continue

                    seen.add(v3)
                    union(v2,v3)
                    bfs.append(v3)
                    
            ans[find(v)] = ans2
            
        return [0 if v1 == v2 else (ans[find(v1)] if find(v1) == find(v2) else -1) for v1,v2 in query]
