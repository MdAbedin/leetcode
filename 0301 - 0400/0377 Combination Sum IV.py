class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(s):
            if s == 0: return 1
            if s < 0: return 0
            return sum(solve(s-num) for num in nums)

        return solve(target)
