class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]
        streak = 0
        ans = 0
        prev = -1

        for c in colors:
            if c == prev: streak = 1
            else: streak += 1

            if streak >= k: ans += 1
            prev = c

        return ans
