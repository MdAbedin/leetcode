class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        seen = set()
        ans = -1

        for start in range(len(edges)):
            path = []
            cur = start

            while cur not in seen and cur != -1:
                seen.add(cur)
                path.append(cur)
                cur = edges[cur]

            if cur in path: ans = max(ans, len(path) - path.index(cur))

        return ans
