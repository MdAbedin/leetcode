class NumArray:
    def __init__(self, nums: List[int]):
        self.ps = [0]+list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right+1]-self.ps[left]
