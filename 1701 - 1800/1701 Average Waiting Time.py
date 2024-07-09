class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        times = []
        t = 0

        for arrival,time in customers:
            t = max(t,arrival)
            times.append(t+time-arrival)
            t += time

        return mean(times)
