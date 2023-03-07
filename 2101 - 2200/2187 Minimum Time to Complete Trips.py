class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return bisect_left(range(10**14+1), totalTrips, key = lambda t: sum(t//bus for bus in time))
