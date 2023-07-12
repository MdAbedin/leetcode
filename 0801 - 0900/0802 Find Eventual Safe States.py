class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        G2 = [[] for i in range(len(graph))]

        for i in range(len(graph)):
            for nei in graph[i]: G2[nei].append(i)

        out_degrees = {i:len(graph[i]) for i in range(len(graph))}
        tsort = [i for i in range(len(graph)) if out_degrees[i] == 0]
        ans = []

        while tsort:
            node = tsort.pop()
            ans.append(node)

            for nei in G2[node]:
                out_degrees[nei] -= 1
                if out_degrees[nei] == 0: tsort.append(nei)

        return sorted(ans)
