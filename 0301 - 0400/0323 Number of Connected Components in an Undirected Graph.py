class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        neighbors = defaultdict(set)
        seen = set()
        
        for a,b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
            
        for i in range(n):
            if i not in seen:
                ans += 1
                
                bfs = deque([i])
                
                while bfs:
                    cur = bfs.popleft()
                    seen.add(cur)
                    
                    for neighbor in neighbors[cur]:
                        if neighbor not in seen:
                            bfs.append(neighbor)
                            
        return ans
