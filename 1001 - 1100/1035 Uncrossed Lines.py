class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(i,j):
            if i == len(nums1) or j == len(nums2): return 0
            return 1+solve(i+1,j+1) if nums1[i] == nums2[j] else max(solve(i+1,j),solve(i,j+1))

        return solve(0,0)
