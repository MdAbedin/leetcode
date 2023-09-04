class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def is_palindrome(l,r): return True if l > r else s[l]==s[r] and is_palindrome(l+1,r-1)

        @cache
        def solve(i): return 0 if i == len(s) else 1+min(solve(i2) for i2 in range(i+1,len(s)+1) if is_palindrome(i,i2-1))

        return solve(0)-1
