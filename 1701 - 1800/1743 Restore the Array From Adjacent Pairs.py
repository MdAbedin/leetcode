class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for v1,v2 in adjacentPairs:
            g[v1].append(v2)
            g[v2].append(v1)

        ans = []
        cur = [num for num in g if len(g[num]) == 1][0]
        seen = set()

        while True:
            ans.append(cur)
            seen.add(cur)
            if g[cur][0] not in seen: cur = g[cur][0]
            elif len(g[cur]) == 2 and g[cur][1] not in seen: cur = g[cur][1]
            else: break

        return ans
