class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def solve(i,j):
            if j == len(p): return i == len(s)

            if p[j] == "?": return i < len(s) and solve(i+1,j+1)
            elif p[j] == "*": return any(solve(i2,j+1) for i2 in range(i,len(s)+1))
            else: return i < len(s) and s[i] == p[j] and solve(i+1,j+1)

        return solve(0,0)
