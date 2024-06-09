class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter({0:1})
        ps = 0
        ans = 0

        for num in nums:
            ps += num
            ans += counts[ps%k]
            counts[ps%k] += 1

        return ans
