class Solution:
    def addBinary(self, a: str, b: str) -> str:
      max_len = max(len(a), len(b))
      
      return bin(int('0'*(max_len-len(a))+a, 2) + int('0'*(max_len-len(b))+b, 2))[2:]
