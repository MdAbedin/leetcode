class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def solve(i1,i2): return True if i1 >= i2 else s[i1] == s[i2] and solve(i1+1,i2-1)
        return sum(solve(i1,i2) for i1 in range(len(s)) for i2 in range(i1,len(s)))
