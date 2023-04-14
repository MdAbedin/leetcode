class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def helper(l,r):
            if l >= r: return r-l+1
            return (2 + helper(l+1,r-1)) if s[l] == s[r] else max(helper(l+1,r), helper(l,r-1))

        return helper(0,len(s)-1)
