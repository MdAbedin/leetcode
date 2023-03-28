class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_words = {tuple(sorted(w)) for w in startWords}
        return sum(any(tuple(sorted(set(w) - {c})) in start_words for c in w) for w in targetWords)
