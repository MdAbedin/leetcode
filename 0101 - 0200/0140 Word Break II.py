class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def solve(i):
            if i == len(s): return [""]
            if i > len(s): return []
            return [(w + " " + ans).rstrip() for w in wordDict for ans in solve(i+len(w)) if s.startswith(w,i)]

        return solve(0)
