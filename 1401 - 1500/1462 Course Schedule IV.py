class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)
        is_prereq = defaultdict(lambda:False)

        for v1,v2 in prerequisites: g[v1].append(v2)

        for v in range(numCourses):
            bfs = [v]
            seen = {v}

            for v2 in bfs:
                is_prereq[v,v2] = True

                for v3 in g[v2]:
                    if v3 in seen: continue
                    seen.add(v3)
                    bfs.append(v3)

        return [is_prereq[v1,v2] for v1,v2 in queries]
