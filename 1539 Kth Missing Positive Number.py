class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 1
        
        for num in arr:
          while ans != num:
            k -= 1
            if k == 0: return ans
            ans += 1
          ans += 1
            
        return ans+k-1
