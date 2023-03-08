class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return 1+bisect_left(range(1,max(piles)*len(piles)+1), -h, key = lambda k: -sum(ceil(pile/k) for pile in piles))
