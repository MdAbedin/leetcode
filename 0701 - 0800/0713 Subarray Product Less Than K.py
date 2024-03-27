class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        r = 0
        ans = 0

        for l in range(len(nums)):
            r = max(r,l)

            while r < len(nums) and p*nums[r] < k:
                p *= nums[r]
                r += 1

            ans += r-l
            if r > l: p //= nums[l]

        return ans
