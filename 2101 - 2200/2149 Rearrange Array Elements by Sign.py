class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return chain(*zip(sorted(nums,key=lambda x: x < 0)[:len(nums)//2], sorted(nums,key=lambda x: x < 0)[len(nums)//2:]))
