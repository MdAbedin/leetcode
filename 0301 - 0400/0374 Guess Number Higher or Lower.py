class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n+1),0,key = lambda x: -guess(x))
