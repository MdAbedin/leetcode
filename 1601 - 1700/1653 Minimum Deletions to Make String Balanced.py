class Solution:
    def minimumDeletions(self, s: str) -> int:
        a,b = s.count("a"),0
        ans = a

        for c in s:
            if c == "a": a -= 1
            else: b += 1
            ans = min(ans,a+b)

        return ans
