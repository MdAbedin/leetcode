class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def fails(l):
            if l == 0: return False
            
            cost = sum(abs(ord(c1)-ord(c2)) for c1,c2 in zip(s[:l-1],t[:l-1]))

            for i in range(l-1,len(s)):
                cost += abs(ord(s[i])-ord(t[i]))
                if cost <= maxCost: return False
                cost -= abs(ord(s[i-(l-1)])-ord(t[i-(l-1)]))

            return True

        return bisect_left(range(len(s)+1),True,key=fails)-1
