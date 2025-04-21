class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        return max(0,(upper-lower)-(max(accumulate([0]+differences))-min(accumulate([0]+differences)))+1)
