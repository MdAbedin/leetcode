class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def solve(i): return True if i == len(s) else any(s.startswith(word,i) and solve(i+len(word)) for word in wordDict)
        return solve(0)
