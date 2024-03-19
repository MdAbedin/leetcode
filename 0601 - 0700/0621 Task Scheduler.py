class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return max(len(tasks),(max(Counter(tasks).values())-1)*(n+1)+list(Counter(tasks).values()).count(max(Counter(tasks).values())))
