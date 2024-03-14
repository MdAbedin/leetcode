class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = Counter({0:1})
        ps = ans = 0

        for num in nums:
            ps += num
            ans += counts[ps-goal]
            counts[ps] += 1

        return ans
