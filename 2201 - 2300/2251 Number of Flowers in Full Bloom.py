class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diffs = defaultdict(int)
        times = set()

        for s,e in flowers:
            diffs[s] += 1
            diffs[e+1] -= 1
            times |= {s,e+1}

        ans = {}
        f = 0

        for t in sorted(times|set(persons)):
            f += diffs[t]
            ans[t] = f

        return map(ans.__getitem__,persons)
