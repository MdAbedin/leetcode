class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ssum_locs = {0: -1}
        ans = 0
        ssum = 0
        
        for i in range(len(nums)):
            ssum += 1 if nums[i] == 1 else -1
            if ssum in ssum_locs:
                ans = max(ans, i - ssum_locs[ssum])
            else:
                ssum_locs[ssum] = i
                
        return ans
