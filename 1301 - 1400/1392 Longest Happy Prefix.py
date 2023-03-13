class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix_hashes = set()
        prefix_hash = 0
        MOD = 10**9+7
        
        for i in range(len(s)-1):
            prefix_hash *= 27
            prefix_hash += ord(s[i]) - ord("a") + 1
            prefix_hash %= MOD
            prefix_hashes.add(prefix_hash)

        ans = []
        suffix_hash = 0

        for i in range(len(s)):
            suffix_hash += (ord(s[~i]) - ord("a") + 1) * pow(27,i,MOD)
            suffix_hash %= MOD

            if suffix_hash in prefix_hashes: ans.append(i+1)

        if not ans: return ""

        for length in reversed(ans):
            if s[:length] == s[-length:]: return s[:length]

        return ""
