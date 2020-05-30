class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(set)
        in_degrees = defaultdict(int)
        edges = len(prerequisites)
        
        for a,b in prerequisites:
            neighbors[a].add(b)
            in_degrees[b] += 1
            
        tsort = deque([i for i in range(numCourses) if i not in in_degrees])
        
        while tsort:
            cur = tsort.popleft()
            remove = set()
            
            for neighbor in neighbors[cur]:
                in_degrees[neighbor] -= 1
                edges -= 1
                if in_degrees[neighbor] == 0:
                    tsort.append(neighbor)
                remove.add(neighbor)
            neighbors[cur] -= remove
                
        return edges == 0
