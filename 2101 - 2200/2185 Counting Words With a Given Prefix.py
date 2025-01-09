class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(x.startswith(pref) for x in words)
