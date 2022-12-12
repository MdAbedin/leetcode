class Solution:
    def findKthBit(self, n: int, k: int) -> str:
      s = '0'
      
      for i in range(1,n):
        s = s + '1' + ''.join('0' if s[i] == '1' else '1' for i in range(len(s)))[::-1]
        
      return s[k-1]
