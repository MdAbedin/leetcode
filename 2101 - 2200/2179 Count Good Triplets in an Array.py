class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        inds = {num:i for i,num in enumerate(nums1)}
        sl = SortedList()
        ans = 0

        for i,num in enumerate(nums2):
            less = sl.bisect_left(inds[num])
            ans += less*(len(nums2)-1-i-(inds[num]-less))
            sl.add(inds[num])

        return ans
