class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((x1+x2)%2 for x1,x2 in pairwise(nums))
