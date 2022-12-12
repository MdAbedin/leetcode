class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        neighbors = defaultdict(set)
        for a,b in dislikes:
            neighbors[a].add(b)
            neighbors[b].add(a)
            
        colors = defaultdict(int)
        
        for i in range(1,N+1):
            if colors[i] == 0:
                colors[i] = 1
                
                bfs = deque([i])
                
                while bfs:
                    for j in range(len(bfs)):
                        cur = bfs.popleft()
                        
                        for neighbor in neighbors[cur]:
                            if colors[neighbor] == colors[cur]:
                                return False
                            if colors[neighbor] == 0:
                                colors[neighbor] = 3-colors[cur]
                                bfs.append(neighbor)
            
        return True
