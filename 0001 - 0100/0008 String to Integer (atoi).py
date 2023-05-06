class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = -1 if s and s[0] == "-" else 1
        ans = 0

        for i in range(1 if s and s[0] in "+-" else 0,len(s)):
            if not s[i].isdigit(): break
            ans *= 10
            ans += int(s[i])

        return max(-2**31, min(2**31-1, sign * ans))
