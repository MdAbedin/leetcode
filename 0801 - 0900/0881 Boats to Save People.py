from sortedcontainers import SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        sl = SortedList(people)

        while sl:
            heaviest = sl.pop()
            if (match_i := sl.bisect_right(limit-heaviest)-1) in range(len(sl)): sl.pop(match_i)
            ans += 1

        return ans
