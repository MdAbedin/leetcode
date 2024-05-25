class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def solve(i): return [[]] if i == len(s) else [[word,*ans] for word in wordDict if s.startswith(word,i) for ans in solve(i+len(word))]
        return [" ".join(words) for words in solve(0)]
