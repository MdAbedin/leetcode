class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern): return False
        pairs = list(zip(pattern,words))
        return all(all((c,w) == (c2,w2) for c2,w2 in pairs if c == c2 or w == w2) for c,w in pairs)
