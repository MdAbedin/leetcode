from numpy import sign

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return sign(prod(nums))
