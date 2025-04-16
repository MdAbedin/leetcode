class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = Counter()
        good = 0
        r = 0
        ans = 0

        for l in range(len(nums)):
            while r < len(nums) and good < k:
                good += counts[nums[r]]
                counts[nums[r]] += 1
                r += 1

            if good >= k: ans += len(nums)-r+1
            good -= counts[nums[l]]-1
            counts[nums[l]] -= 1

        return ans
