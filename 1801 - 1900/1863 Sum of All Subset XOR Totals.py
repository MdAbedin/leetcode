class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(xor,s) for l in range(1,len(nums)+1) for s in combinations(nums,l))
