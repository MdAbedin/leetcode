class Solution:
    def punishmentNumber(self, n: int) -> int:
        def works(s,num):
            if num < 0: return False
            if s == "": return num == 0
            if num == 0: return set(s) == {"0"}
            return any(works(s[i:],num-int(s[:i])) for i in range(1,len(s)+1))
        
        return sum(num**2 for num in range(1,n+1) if works(str(num**2),num))
