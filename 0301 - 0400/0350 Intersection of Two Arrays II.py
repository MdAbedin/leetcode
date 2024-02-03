class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2 = map(Counter,[nums1,nums2])
        return sum([[num]*min(c1[num],c2[num]) for num in c1],start=[])
