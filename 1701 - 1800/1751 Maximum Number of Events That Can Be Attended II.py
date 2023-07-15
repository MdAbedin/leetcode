class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])
        ends = [e for s,e,v in events]

        dp = [[0]*(k+1)]
        dp[0][1] = events[0][2]

        for i in range(1,len(events)):
            dp2 = dp[-1][:]
            dp2[1] = max(dp2[1],events[i][2])

            if (i2 := bisect_left(ends,events[i][0])-1) >= 0:
                for count in range(2,k+1): dp2[count] = max(dp2[count], dp[i2][count-1] + events[i][2])

            dp.append(dp2)

        return max(dp[-1])
