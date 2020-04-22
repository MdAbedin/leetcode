class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        neighbors = defaultdict(list)
        probs = dict()
        
        for edge in edges:
            a,b = edge
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        bfs = deque([1])
        probs[1] = 1
        
        while bfs and t:
            for i in range(len(bfs)):
                cur = bfs.popleft()
                num_unvisited_neighbors = 0

                for neighbor in neighbors[cur]:
                    if neighbor not in probs:
                        num_unvisited_neighbors += 1
                        bfs.append(neighbor)

                for neighbor in neighbors[cur]:
                    if neighbor not in probs:
                        probs[neighbor] = probs[cur]/num_unvisited_neighbors

                if num_unvisited_neighbors:
                    probs[cur] = 0

            t -= 1
        
        return probs[target] if target in probs else 0
