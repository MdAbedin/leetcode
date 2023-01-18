class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        prefix_sum, suffix_sum = 0, sum(nums)
        min_prefix_sum, max_prefix_sum = 0, 0
        ans = -inf
        
        for num in nums:
            prefix_sum += num
            
            ans = max(ans, prefix_sum - min_prefix_sum, suffix_sum + max_prefix_sum)
            
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
            suffix_sum -= num
        
        return ans
