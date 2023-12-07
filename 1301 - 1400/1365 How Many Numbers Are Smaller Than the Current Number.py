class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    return [sum(nums[i2] < num for i2 in range(len(nums)) if i2 != i) for i,num in enumerate(nums)]
