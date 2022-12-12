class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        vertex_x = -1*b/(2*a) if a != 0 else nums[0]
        lefts, rights = nums[::], []
        
        for i in range(len(nums)):
          if nums[i] >= vertex_x:
            lefts, rights = nums[:i], nums[i:]
            break
            
        for i in range(len(lefts)):
          lefts[i] = a*(lefts[i])**2 + b*lefts[i] + c
          
        for i in range(len(rights)):
          rights[i] = a*(rights[i])**2 + b*rights[i] + c
          
        if a < 0:
          lefts = lefts[::-1]
          rights = rights[::-1]
        if a == 0 and b < 0:
          rights = rights[::-1]
          
        ans = [0]*len(nums)
        li, ri = 0, 0
        
        for i in range(len(ans)):
          if li >= len(lefts) or (ri < len(rights) and rights[ri] <= lefts[-1*li-1]):
            ans[i] = rights[ri]
            ri += 1
          else:
            ans[i] = lefts[-1*li-1]
            li += 1
        
        return ans
