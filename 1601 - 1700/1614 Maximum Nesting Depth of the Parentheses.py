class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        ans = 0

        for c in s:
            if c == "(": d += 1
            elif c == ")": d -= 1
            ans = max(ans,d)

        return ans
