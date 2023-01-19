class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_mod_counts = Counter({0:1})
        prefix_sum_mod = 0
        ans = 0
        
        for num in nums:
            prefix_sum_mod += num
            prefix_sum_mod %= k
            
            ans += prefix_sum_mod_counts[prefix_sum_mod]
            
            prefix_sum_mod_counts[prefix_sum_mod] += 1
        
        return ans
