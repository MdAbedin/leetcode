class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = sorted(nums)
        ans = 0

        while pq[0] < k:
            x1,x2 = heappop(pq),heappop(pq)
            heappush(pq,min(x1,x2)*2+max(x1,x2))
            ans += 1

        return ans
