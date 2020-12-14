class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        
        for num in nums:
            if num-1 not in nums:
                end_num = num
                while end_num+1 in nums:
                    end_num += 1
                ans = max(ans, end_num-num+1)
        
        return ans
