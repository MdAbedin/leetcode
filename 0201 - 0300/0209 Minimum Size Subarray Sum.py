class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = sum(nums)
        if s < target: return 0

        ans = len(nums)
        r = len(nums)-1

        for l in range(len(nums)):
            while r > l and s-nums[r] >= target:
                s -= nums[r]
                r -= 1
            
            if s >= target: ans = r-l+1

            s -= nums[l]
            
            if r+1 < len(nums):
                r += 1
                s += nums[r]

        return ans
