class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ls,rs = 0,sum(nums)
        ri = 0
        ans = len(nums) if rs == x else inf

        for i,num in enumerate(nums):
            while ri < len(nums) and (ri < i or ls+rs-nums[ri] >= x):
                rs -= nums[ri]
                ri += 1

            if ls+rs == x: ans = min(ans,i+len(nums)-ri)
            ls += nums[i]

        return -1 if ans == inf else ans
