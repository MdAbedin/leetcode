class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        return sum(comb(c,2) for c in Counter(num-int(str(num)[::-1]) for num in nums).values())%(10**9+7)
