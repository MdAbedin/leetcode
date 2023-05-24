class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        data = sorted([[n2,n1] for n1,n2 in zip(nums1,nums2)],reverse=True)
        pq = [data[i][1] for i in range(k)]
        heapify(pq)
        s = sum(pq)
        ans = s*data[k-1][0]

        for i in range(k,len(nums1)):
            s += data[i][1] - heappushpop(pq,data[i][1])
            ans = max(ans,s*data[i][0])

        return ans
