class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [[nums1[i]+nums2[0],i,0] for i in range(len(nums1))]
        heapify(pq)
        ans = []

        for i in range(min(k,len(nums1)*len(nums2))):
            s,i1,i2 = heappop(pq)
            ans.append([nums1[i1],nums2[i2]])
            if i2+1 < len(nums2): heappush(pq, [nums1[i1]+nums2[i2+1],i1,i2+1])

        return ans
