class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def fails(l):
            pq1,pq2 = [],[]

            for i,n in enumerate(nums):
                heappush(pq1,(n,i))
                heappush(pq2,(-n,i))
                while pq1[0][1] < i-l+1: heappop(pq1)
                while pq2[0][1] < i-l+1: heappop(pq2)

                if i >= l-1 and -pq2[0][0] - pq1[0][0] <= limit: return False

            return True

        return bisect_left(range(1,len(nums)+1),True,key=fails)
