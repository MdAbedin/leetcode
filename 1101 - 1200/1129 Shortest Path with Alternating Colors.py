class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in redEdges: graph[a].append([b,"red"])
        for a,b in blueEdges: graph[a].append([b,"blue"])

        ans = [inf]*n
        bfs = deque([[0,"red"],[0,"blue"]])
        seen = {(0,"red"),(0,"blue")}
        dist = 0

        while bfs:
            for i in range(len(bfs)):
                node,color = bfs.popleft()
                ans[node] = min(ans[node],dist)

                for nei,color2 in graph[node]:
                    if (nei,color2) not in seen and color2 != color:
                        seen.add((nei,color2))
                        bfs.append([nei,color2])

            dist += 1

        return [-1 if x == inf else x for x in ans]
