class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        pair_sums = sorted(list(map(sum, pairwise(weights))))
        return sum(pair_sums[-(k-1):]) - sum(pair_sums[:k-1])
