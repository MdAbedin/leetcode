class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return {tuple(sorted(subset)) for size in range(len(nums)+1) for subset in combinations(nums,size)}
