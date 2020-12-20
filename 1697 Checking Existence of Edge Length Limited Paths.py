class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = defaultdict(list)
        dists = set()
        for u,v,d in edgeList:
            edges[d].append([u,v])
            dists.add(d)
            
        dists = sorted(list(dists))
        di = 0
        leaders = {x:x for x in range(n)}
        followers = {x:[x] for x in range(n)}
        
        ans = [False]*len(queries)
        queries = sorted([queries[i] + [i] for i in range(len(queries))], key = lambda x: x[2])
        
        for p,q,l,i in queries:
            while di < len(dists) and dists[di] < l:
                for u,v in edges[dists[di]]:
                    if leaders[u] != leaders[v]:
                        old = leaders[u] if len(followers[leaders[u]]) < len(followers[leaders[v]]) else leaders[v]
                        new = leaders[u] if old!=leaders[u] else leaders[v]
                        
                        for x in followers[old]:
                            leaders[x] = new

                        followers[new] += followers[old]
                        followers[old] = []
                        
                di += 1

            ans[i] = leaders[p] == leaders[q]
            
        return ans
