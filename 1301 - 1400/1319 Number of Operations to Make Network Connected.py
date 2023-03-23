class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1

        neighbors = defaultdict(list)

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        components = 0
        seen = set()

        for node in range(n):
            if node in seen: continue

            components += 1
            seen.add(node)
            dfs = [node]

            while dfs:
                cur = dfs.pop()

                for neighbor in neighbors[cur]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        dfs.append(neighbor)

        return components-1
