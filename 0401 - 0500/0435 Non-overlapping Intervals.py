class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: [pair[1],pair[0]])
        dp = []

        for i,(s,e) in enumerate(intervals):
            i1 = bisect_right(intervals,s,key=lambda pair: pair[1])-1
            dp.append(min(1 + (dp[-1] if dp else 0),(dp[i1] if i1 >= 0 else 0) + i-i1-1))

        return dp[-1]
