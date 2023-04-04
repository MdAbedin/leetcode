class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        chars = set()

        for c in s:
            if c in chars:
                ans += 1
                chars = {c}
            else:
                chars.add(c)

        if chars: ans += 1

        return ans
