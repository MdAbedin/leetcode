class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return [num for x1,x2,num in sorted([r+c,-r,nums[r][c]] for r in range(len(nums)) for c in range(len(nums[r])))]
