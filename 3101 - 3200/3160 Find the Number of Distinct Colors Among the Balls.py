class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        counts = Counter()
        ans = []

        for x,y in queries:
            if x in colors:
                counts[colors[x]] -= 1
                if counts[colors[x]] == 0: counts.pop(colors[x])

            colors[x] = y
            counts[y] += 1
            ans.append(len(counts))

        return ans
