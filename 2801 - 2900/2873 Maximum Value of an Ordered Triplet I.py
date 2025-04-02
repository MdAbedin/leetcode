class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        return max(0,max((nums[i1]-nums[i2])*nums[i3] for i1,i2,i3 in combinations(range(len(nums)),3)))
