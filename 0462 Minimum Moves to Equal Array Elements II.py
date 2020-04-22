class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        
        return reduce(lambda a,b: a+abs(median-b), nums, 0)
