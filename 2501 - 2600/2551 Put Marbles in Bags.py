class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_sums = sorted(list(map(sum,pairwise(weights))))
        return sum(pair_sums[len(pair_sums)-k+1:])-sum(pair_sums[:k-1])
