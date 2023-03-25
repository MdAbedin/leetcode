class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        S = sum(nums)
        ans = sum(i*num for i,num in enumerate(nums))
        cur_ans = ans

        for i in range(len(nums)-1):
            cur_ans -= nums[~i] * (len(nums)-1)
            cur_ans += S - nums[~i]
            ans = max(ans,cur_ans)

        return ans
