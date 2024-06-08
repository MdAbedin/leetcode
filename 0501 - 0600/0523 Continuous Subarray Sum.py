class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        inds = {0:-1}
        return any(inds.setdefault(s%k,i) <= i-2 for i,s in enumerate(accumulate(nums)))
