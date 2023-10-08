class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(i1,i2): return 0 if i1 == len(nums1) or i2 == len(nums2) else max(nums1[i1]*nums2[i2] + solve(i1+1,i2+1),solve(i1+1,i2),solve(i1,i2+1))

        return max(nums1[i1]*nums2[i2] + solve(i1+1,i2+1) for i1 in range(len(nums1)) for i2 in range(len(nums2)))
