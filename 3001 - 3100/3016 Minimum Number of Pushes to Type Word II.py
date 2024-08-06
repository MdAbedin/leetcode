class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(c*(i//8+1) for i,c in enumerate(sorted(Counter(word).values(),reverse=True)))
