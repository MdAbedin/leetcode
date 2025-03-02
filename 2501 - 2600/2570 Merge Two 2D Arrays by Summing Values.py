class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        vals1,vals2 = defaultdict(int,nums1),defaultdict(int,nums2)
        return [[ID,vals1[ID]+vals2[ID]] for ID in sorted(set(vals1)|set(vals2))]
