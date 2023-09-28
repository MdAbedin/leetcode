class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums,key=lambda num: num%2)
