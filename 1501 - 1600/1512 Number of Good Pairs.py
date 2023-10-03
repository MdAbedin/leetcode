class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(comb(c,2) for c in Counter(nums).values())
