class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def furthest(v,g):
            bfs = [[v,0]]
            seen = {v}

            for v2,d in bfs:
                for v3 in g[v2]:
                    if v3 in seen: continue
                    seen.add(v3)
                    bfs.append((v3,d+1))
                    
            return bfs[-1]
        
        g1 = defaultdict(list)
        
        for v1,v2 in edges1:
            g1[v1].append(v2)
            g1[v2].append(v1)

        g2 = defaultdict(list)
        
        for v1,v2 in edges2:
            g2[v1].append(v2)
            g2[v2].append(v1)

        v1,d1 = furthest(0,g1)
        v2,d2 = furthest(v1,g1)
        
        v3,d3 = furthest(0,g2)
        v4,d4 = furthest(v3,g2)
        
        return max(d2,d4,ceil(d2/2)+1+ceil(d4/2))
