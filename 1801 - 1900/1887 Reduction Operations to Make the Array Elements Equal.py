class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        return sum(accumulate(count for num,count in sorted(Counter(nums).items(),reverse=True))) - len(nums)
