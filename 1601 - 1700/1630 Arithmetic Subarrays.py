class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [len({num2-num1 for num1,num2 in pairwise(sorted(nums[left:right+1]))}) == 1 for left,right in zip(l,r)]
