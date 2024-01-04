class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums).values()
        if 1 in counts: return -1
        return sum(c//3+(c%3 != 0) for c in counts)
