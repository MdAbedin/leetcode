class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(c for c1,c2 in zip_longest(word1,word2,fillvalue="") for c in [c1,c2])
