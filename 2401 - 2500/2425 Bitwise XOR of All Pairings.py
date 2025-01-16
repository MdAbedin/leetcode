class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return (reduce(xor,nums1) if len(nums2)%2 == 1 else 0) ^ (reduce(xor,nums2) if len(nums1)%2 == 1 else 0)
