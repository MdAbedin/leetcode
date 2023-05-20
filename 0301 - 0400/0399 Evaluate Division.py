class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
    
        for (var1,var2),val in zip(equations,values):
            g[var1][var2] = val
            g[var2][var1] = 1/val

        def solve(start,end,seen): 
            if start not in g: return -1
            if start == end: return 1
            
            seen.add(start)
            
            for nei in g[start]:
                if nei in seen: continue
                if (ans := solve(nei,end,seen)) != -1: return g[start][nei]*ans

            return -1

        return [solve(var1,var2,set()) for var1,var2 in queries]
