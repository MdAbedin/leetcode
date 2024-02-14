class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            while nums[num-1] != num:
                num2 = nums[num-1]
                nums[num-1] = num
                num = num2

        return [i+1 for i,num in enumerate(nums) if num != i+1]
