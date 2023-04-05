class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        psums = list(accumulate(nums))
        return bisect_left(range(psums[-1]+1), True, key = lambda x: all(x*(i+1) >= psums[i] for i in range(len(psums))))
