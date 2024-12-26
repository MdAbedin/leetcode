class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = Counter({0:1})

        for num in nums:
            counts2 = Counter()

            for s,c in counts.items():
                counts2[s] += c
                counts2[s+num] += c

            counts = counts2

        return counts[(sum(nums)+target)/2]
