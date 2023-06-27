class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(map(tuple,permutations(nums)))
