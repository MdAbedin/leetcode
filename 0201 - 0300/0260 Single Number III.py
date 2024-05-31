class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = reduce(xor,nums)
        b = xor_all
        
        for num in nums:
            if num < xor_all^num: b ^= num
                
        return [xor_all^b,b]
