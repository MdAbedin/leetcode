class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nodes_from = defaultdict(list)
        nodes_to = defaultdict(list)

        for f,t in connections:
            nodes_from[f].append(t)
            nodes_to[t].append(f)

        ans = 0
        seen = {0}
        dfs = [0]

        while dfs:
            node = dfs.pop()

            for node2 in nodes_from[node]:
                if node2 not in seen:
                    seen.add(node2)
                    dfs.append(node2)
                    ans += 1

            for node2 in nodes_to[node]:
                if node2 not in seen:
                    seen.add(node2)
                    dfs.append(node2)

        return ans
