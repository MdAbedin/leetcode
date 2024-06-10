class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(starmap(ne,zip(heights,sorted(heights))))
