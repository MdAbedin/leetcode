class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return max(num1+num2 for num1,num2 in zip(sorted(nums),sorted(nums,reverse=True)))
