class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_left = Counter()
        G2 = defaultdict(list)

        for a,b in prerequisites:
            prereqs_left[a] += 1
            G2[b].append(a)

        tsort = [i for i in range(numCourses) if prereqs_left[i] == 0]

        while tsort:
            node = tsort.pop()

            for nei in G2[node]:
                prereqs_left[nei] -= 1
                if prereqs_left[nei] == 0: tsort.append(nei)

        return set(prereqs_left.values()).issubset({0})
