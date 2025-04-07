class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        diffs = {0}
        for num in nums: diffs = {d+add for d in diffs for add in [num,-num]}
        return 0 in diffs
