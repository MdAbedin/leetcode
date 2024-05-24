class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        return max(sum(map(score.__getitem__,map(ascii_lowercase.find,chain(*ss)))) for l in range(len(words)+1) for ss in combinations(words,l) if Counter(chain(*ss)) <= Counter(letters))
