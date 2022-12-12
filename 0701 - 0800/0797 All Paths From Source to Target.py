class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dfs = deque([0])
        ans = []
        path = deque()
        seen = set()
        
        while dfs:
            cur = dfs[-1]
            
            if cur not in seen:
                seen.add(cur)
                path.append(cur)
            
                if cur == len(graph)-1:
                    ans.append(list(path))
                else:
                    for child in graph[cur]:
                        dfs.append(child)
            else:
                dfs.pop()
                path.pop()
                seen.remove(cur)
        
        return ans
