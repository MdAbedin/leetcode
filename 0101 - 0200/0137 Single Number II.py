class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        min_num = min(0, min(nums))
        
        for i in range(len(nums)):
            nums[i] -= min_num
            
        max_bin = ['0']*len(bin(max(nums))[2:])
        
        for num in nums:
            num_bin = bin(num)[2:]
            num_bin = '0'*(len(max_bin)-len(num_bin)) + num_bin
            
            for i in range(len(max_bin)):
                max_bin[i] = str((int(max_bin[i]) + int(num_bin[i])) % 3)
                
        return int(''.join(max_bin), base=2)+min_num
