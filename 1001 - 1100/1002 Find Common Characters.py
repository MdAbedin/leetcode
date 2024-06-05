class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return sum([[c]*min(w.count(c) for w in words) for c in ascii_lowercase],[])
