class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = list(Counter(nums).values())
        return counts.count(max(counts))*max(counts)
