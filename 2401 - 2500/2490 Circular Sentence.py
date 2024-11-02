class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return all(w1[-1] == w2[0] for w1,w2 in pairwise(sentence.split()*2))
