class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(c := Counter(nums),key = c.__getitem__)
