class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def solve(i,d):
            if d == 1: return max(jobDifficulty[i2] for i2 in range(i,len(jobDifficulty)))

            m = jobDifficulty[i]
            ans = inf

            for i2 in range(i+1,len(jobDifficulty)):
                ans = min(ans,m+solve(i2,d-1))
                m = max(m,jobDifficulty[i2])

            return ans

        return -1 if (ans := solve(0,d)) == inf else ans
