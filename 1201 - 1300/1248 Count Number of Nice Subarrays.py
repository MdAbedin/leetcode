class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans,odds = 0,0
        counts = Counter({0:1})

        for num in nums:
            odds += num%2
            ans += counts[odds-k]
            counts[odds] += 1

        return ans
