class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = set()

        for start in range(len(graph)):
            if start in seen: continue

            seen.add(start)
            bfs = deque([start])

            while bfs:
                level = set(bfs)

                for i in range(len(bfs)):
                    node = bfs.popleft()

                    for node2 in graph[node]:
                        if node2 in level: return False
                        
                        if node2 not in seen:
                            seen.add(node2)
                            bfs.append(node2)

        return True
