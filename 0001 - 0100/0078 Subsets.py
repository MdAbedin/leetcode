class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [subset for size in range(len(nums)+1) for subset in combinations(nums,size)]
