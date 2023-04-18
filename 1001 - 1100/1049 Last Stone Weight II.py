class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return min(abs(sum(stones) - 2*subset_sum) for subset_sum in reduce(lambda subset_sums,stone: {subset_sum+add for subset_sum in subset_sums for add in [0,stone]}, stones, {0}))
