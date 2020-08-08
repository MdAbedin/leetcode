class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      ans = []
      
      for i in range(2**len(nums)):
        bitmask = bin(i)[2:]
        bitmask = '0'*(len(nums)-len(bitmask)) + bitmask
        
        ans.append([nums[j] for j in range(len(nums)) if bitmask[j] == '1'])
        
      return ans
