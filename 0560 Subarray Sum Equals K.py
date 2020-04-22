class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        cum_sum = 0
        ans = 0
        
        for num in nums:
            cum_sum += num
            
            if cum_sum-k in sums:
                ans += sums[cum_sum-k]
                
            sums[cum_sum] += 1
            
        return ans
