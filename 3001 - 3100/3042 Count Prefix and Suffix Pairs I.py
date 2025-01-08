class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(w2.startswith(w1) and w2.endswith(w1) for w1,w2 in combinations(words,2))
