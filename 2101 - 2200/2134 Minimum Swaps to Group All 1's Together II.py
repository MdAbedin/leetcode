class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c = nums.count(1)
        if c == 0: return 0

        s = sum(nums[:c-1])
        ans = inf

        for i in range(len(nums)):
            s += nums[(i+c-1)%len(nums)]
            ans = min(ans,c-s)
            s -= nums[i]

        return ans
