class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0]+[-1]*n
        pq = []

        for i,length in enumerate(ranges):
            prev = dp[i-length] if i-length >= 0 else 0
            if prev != -1: heappush(pq,[prev+1,i+length])

            while pq and pq[0][1] < i: heappop(pq)

            if pq and i != 0: dp[i] = pq[0][0]

        return dp[-1]
