class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)
        ans = []

        for v1,v2 in prerequisites: g[v1].append(v2)

        for v1,v2 in queries:
            bfs = [v1]
            seen = {v1}

            for v3 in bfs:
                for v4 in g[v3]:
                    if v4 in seen: continue
                    seen.add(v4)
                    bfs.append(v4)

            ans.append(v2 in seen)

        return ans
