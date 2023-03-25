class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        seen = set()
        component_sizes = []

        for node in range(n):
            if node in seen: continue

            seen.add(node)
            dfs = [node]
            size = 0

            while dfs:
                cur = dfs.pop()
                size += 1

                for nei in neighbors[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        dfs.append(nei)

            component_sizes.append(size)

        return sum(size * (n-size) for size in component_sizes)//2
