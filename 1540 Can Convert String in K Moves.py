class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
      if len(s) != len(t): return False
      
      shifts = dict()

      for i in range(len(s)):
        shift = ord(t[i])-ord(s[i])
        
        if shift < 0: shift += 26
        og_shift = shift

        if shift == 0: continue
        if og_shift in shifts: shift = shifts[og_shift]+26
        if shift > k: return False
        
        shifts[og_shift] = shift
        
      return True
