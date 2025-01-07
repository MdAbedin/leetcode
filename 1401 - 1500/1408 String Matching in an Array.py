class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for i,w in enumerate(words) if any(w in w2 for i2,w2 in enumerate(words) if i2 != i) ]
