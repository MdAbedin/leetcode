class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def solve(i):
            if i == len(arr): return 0

            m = -inf
            ans = -inf

            for i2 in range(i,min(len(arr),i+k)):
                m = max(m,arr[i2])
                ans = max(ans,m*(i2-i+1)+solve(i2+1))

            return ans

        return solve(0)
