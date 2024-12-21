class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        
        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
            
        def solve(v,p):
            a,s = 0,values[v]
            
            for nei in g[v]:
                if nei == p: continue
                    
                a2,s2 = solve(nei,v)
                a += a2
                s += s2
            
            return a+(s%k==0),s
        
        return solve(0,None)[0]
