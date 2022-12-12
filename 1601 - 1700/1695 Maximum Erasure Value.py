class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        s = set()
        i,j = 0,0
        cur_ans = 0
        
        while True:
            while j < len(nums) and nums[j] not in s:
                s.add(nums[j])
                cur_ans += nums[j]
                ans = max(ans,cur_ans)
                j += 1
                
            if j == len(nums): break

            s.remove(nums[i])
            cur_ans -= nums[i]
            i += 1
            
        return ans
