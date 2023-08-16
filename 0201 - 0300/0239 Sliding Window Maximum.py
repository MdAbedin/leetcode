class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = [[-num,i] for i,num in enumerate(nums[:k-1])]
        heapify(pq)
        ans = []

        for i in range(k-1,len(nums)):
            heappush(pq,[-nums[i],i])
            while pq[0][1] < i-(k-1): heappop(pq)
            ans.append(-pq[0][0])

        return ans
