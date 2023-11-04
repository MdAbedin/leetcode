class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left,default=-inf),n-min(right,default=inf))
