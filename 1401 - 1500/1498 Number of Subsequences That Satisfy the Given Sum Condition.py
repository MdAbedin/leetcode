class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:

        MOD = 10**9+7

        nums.sort()

        ans = 0

        

        for i,num in enumerate(nums):

            j = bisect_right(nums,target-num)-1

            if j >= i:

                ans += pow(2,j-i,MOD)

                ans %= MOD

        

        return ans
