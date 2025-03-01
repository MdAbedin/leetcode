class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]: continue
            
            nums[i] *= 2
            nums[i+1] = 0

        return [num for num in nums if num != 0] + [0]*nums.count(0)
