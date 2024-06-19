class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def works(d):
            b = 0
            s = 0

            for bd in bloomDay:
                if d >= bd: s += 1
                else: s = 0

                if s >= k:
                    b += 1
                    s = 0

            return b >= m

        ans = bisect_left(range(10**9+1),True,key=works)

        return -1 if ans == 10**9+1 else ans
