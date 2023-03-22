class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(list)

        for a,b,d in roads:
            edges[a].append([b,d])
            edges[b].append([a,d])

        dfs = [1]
        seen = {1}

        while dfs:
            city = dfs.pop()

            for city2,d in edges[city]:
                if city2 not in seen:
                    seen.add(city2)
                    dfs.append(city2)

        return min(min(d for city2,d in edges[city]) for city in seen)
