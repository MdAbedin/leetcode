class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        for v1,v2,c in edges: self.g[v1].append((v2,c))

    def addEdge(self, edge: List[int]) -> None:
        v1,v2,c = edge
        self.g[v1].append((v2,c))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0,node1)]
        dists = defaultdict(lambda:inf)

        while pq:
            d,v = heappop(pq)
            if d > dists[v]: continue
            if v == node2: return d

            for nei,c in self.g[v]:
                if d+c < dists[nei]:
                    dists[nei] = d+c
                    heappush(pq,(d+c,nei))

        return -1
