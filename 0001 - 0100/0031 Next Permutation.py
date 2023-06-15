class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                swap_i = min((j for j in range(i+1,len(nums)) if nums[j] > nums[i]),key = lambda j: nums[j])
                nums[i],nums[swap_i] = nums[swap_i],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return

        nums.reverse()
