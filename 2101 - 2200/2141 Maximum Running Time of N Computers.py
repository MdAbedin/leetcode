class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def fails(t): return sum(min(b,t) for b in batteries) < n*t
        return bisect_left(range(sum(batteries)//n+1),True,key=fails)-1
