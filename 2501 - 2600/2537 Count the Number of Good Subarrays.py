class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        good = 0
        i = 0
        ans = 0
        counts = Counter()
        
        for j in range(len(nums)):
            good += counts[nums[j]]
            counts[nums[j]] += 1
            
            while good - (counts[nums[i]]-1) >= k:
                counts[nums[i]] -= 1
                good -= counts[nums[i]]
                i += 1
            
            if good >= k: ans += i+1
        
        return ans
