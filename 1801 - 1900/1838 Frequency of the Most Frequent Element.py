class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ops_used = 0
        last_i = 0
        ans = 1

        for i in range(1,len(nums)):
            ops_used += (nums[i]-nums[i-1]) * (i - last_i)

            while ops_used > k:
                ops_used -= nums[i] - nums[last_i]
                last_i += 1

            ans = max(ans, i - last_i+1)

        return ans
