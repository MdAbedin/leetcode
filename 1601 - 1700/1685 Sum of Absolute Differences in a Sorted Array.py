class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        r_sum = sum(nums)
        l_sum = 0
        ans = []
        
        for i in range(len(nums)):
            r_sum -= nums[i]
            ans.append(nums[i]*i - l_sum + r_sum - (len(nums)-i-1)*nums[i])
            l_sum += nums[i]
            
        return ans
