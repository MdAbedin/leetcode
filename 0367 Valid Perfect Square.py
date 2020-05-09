class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,ceil(num/2)
        
        while l <= r:
            mid = (l+r)//2
            square = mid**2
            
            if square < num:
                l = mid+1
            elif square > num:
                r = mid-1
            else:
                return True
            
        return False
