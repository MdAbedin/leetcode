class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            heappush(pq,num)
            if len(pq) > k: heappop(pq)

        return pq[0]
