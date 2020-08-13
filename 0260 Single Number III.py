class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = reduce(lambda a,b: a^b, nums)
        b = xor_all
        
        for num in nums:
            num2 = xor_all^num
            
            if num < num2:
                b ^= num
                
        return [xor_all^b, b]
