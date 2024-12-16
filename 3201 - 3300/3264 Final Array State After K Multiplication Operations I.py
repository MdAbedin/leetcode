class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k): nums[min(range(len(nums)),key=nums.__getitem__)] *= multiplier
        return nums
