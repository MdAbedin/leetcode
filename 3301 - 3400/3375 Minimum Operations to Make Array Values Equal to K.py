class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return -1 if min(nums) < k else len(set(nums)-{k})
