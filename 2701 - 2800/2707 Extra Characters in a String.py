class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def solve(i): return 0 if i == len(s) else min(1+solve(i+1),min((solve(i+len(word)) for word in dictionary if s.startswith(word,i)),default=inf))
        return solve(0)
