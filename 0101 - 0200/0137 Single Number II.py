class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = sum(1<<i for i in range(32) if sum((1 if num&(1<<i) else 0) for num in nums)%3 == 1)
        return ans-(1<<32) if ans >= (1<<31) else ans
