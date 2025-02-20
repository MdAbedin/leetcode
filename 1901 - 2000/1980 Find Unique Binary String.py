class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(str(1-int(b[i])) for i,b in enumerate(nums))
