class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i,num in enumerate(nums):
            while num != -1 and nums[num-1] != num: nums[num-1],num = num,nums[num-1]
            if num != -1 and nums[i] != i+1: ans.append(num)
            if nums[i] != i+1: nums[i] = -1

        return ans
