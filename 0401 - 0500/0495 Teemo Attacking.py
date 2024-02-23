class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        last = 0

        for t in timeSeries:
            ans += t+duration - max(t,last)
            last = t+duration

        return ans
