class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for i in range(n)]

        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        def longest_path(v,p):
            ans = [v]

            for v2 in g[v]:
                if v2 == p: continue
                ans = max(ans,longest_path(v2,v)+[v],key=len)

            return ans

        diameter = longest_path(longest_path(0,-1)[0],-1)

        return diameter[(len(diameter)-1)//2:len(diameter)//2+1]
