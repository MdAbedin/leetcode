class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return bisect_left(range(1,10**12+1),True,key = lambda x: sum(c//x for c in candies) < k)
