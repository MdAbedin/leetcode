class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(abs(x1-x2) <= a and abs(x2-x3) <= b and abs(x1-x3) <= c for x1,x2,x3 in combinations(arr,3))
