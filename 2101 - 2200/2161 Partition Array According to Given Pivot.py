class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return sorted(nums,key = lambda num: (num > pivot) - (num < pivot))
