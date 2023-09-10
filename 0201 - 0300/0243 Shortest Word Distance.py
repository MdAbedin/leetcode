class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1,i2 = -inf,-inf
        ans = inf

        for i,w in enumerate(wordsDict):
            if w == word1:
                i1 = i
                ans = min(ans,i-i2)
            if w == word2:
                i2 = i
                ans = min(ans,i-i1)

        return ans
