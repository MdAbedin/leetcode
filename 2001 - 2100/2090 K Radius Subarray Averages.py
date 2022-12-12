class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        psums = [0] + list(accumulate(nums))

        return [-1 if (i-k < 0 or i+k >= len(nums)) else (int((psums[i+k+1] - psums[i-k]) / (2*k+1))) for i in range(len(nums))]
