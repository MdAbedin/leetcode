class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g2 = defaultdict(list)

        for i,neis in enumerate(graph):
            for nei in neis:
                g2[nei].append(i)

        tsort = [i for i,neis in enumerate(graph) if not neis]
        ans = []

        for node in tsort:
            ans.append(node)

            for nei in g2[node]:
                graph[nei].pop()
                if not graph[nei]: tsort.append(nei)

        return sorted(ans)
