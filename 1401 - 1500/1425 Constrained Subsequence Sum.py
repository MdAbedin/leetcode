class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        pq = []
        ans = -inf

        for i,num in enumerate(nums):
            while pq and pq[0][1] < i-k: heappop(pq)
            cur_ans = (0 if not pq else max(0,-pq[0][0])) + num
            ans = max(ans,cur_ans)
            heappush(pq,[-cur_ans,i])

        return ans
