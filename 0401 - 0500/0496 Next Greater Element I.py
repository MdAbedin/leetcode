class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [next((nums2[i] for i in range(nums2.index(x),len(nums2)) if nums2[i] > x),-1) for x in nums1]
