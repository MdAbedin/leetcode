class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(set(nums))[-3:][3%len(sorted(set(nums))[-3:])]
