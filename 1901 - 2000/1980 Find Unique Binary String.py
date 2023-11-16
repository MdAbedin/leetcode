class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        
        for num in range(2**len(nums)):
            if bin(num)[2:].rjust(len(nums),"0") not in nums: return bin(num)[2:].rjust(len(nums),"0")
