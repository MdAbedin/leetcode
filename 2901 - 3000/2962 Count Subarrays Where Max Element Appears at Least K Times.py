class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        c = r = ans = 0
        m = max(nums)

        for l in range(len(nums)):
            while r < len(nums) and c < k:
                c += nums[r] == m
                r += 1

            if c == k: ans += len(nums)-r+1
            c -= nums[l] == m

        return ans
