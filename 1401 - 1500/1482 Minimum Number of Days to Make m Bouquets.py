class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        return -1 if (ans := bisect_left(range(10**9+1),True,key=lambda d: sum(len(list(g))//k for b,g in groupby(bloomDay,key=partial(ge,d)) if b) >= m)) == 10**9+1 else ans
