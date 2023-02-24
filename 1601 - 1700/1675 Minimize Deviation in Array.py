class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        max_num = -inf

        for num in nums:
            end = num*2 if num%2 == 1 else num
            while num%2 == 0: num //= 2
            heappush(pq,[num,end])
            max_num = max(max_num,num)

        ans = max_num - pq[0][0]

        while pq[0][0] != pq[0][1]:
            max_num = max(max_num, pq[0][0]*2)
            heapreplace(pq, [pq[0][0]*2, pq[0][1]])
            ans = min(ans, max_num - pq[0][0])

        return ans
