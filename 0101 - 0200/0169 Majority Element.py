class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        return reduce(lambda a,b: b if counts[b] > len(nums)//2 else a, counts, 0)
