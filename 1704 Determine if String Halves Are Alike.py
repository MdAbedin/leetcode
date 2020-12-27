class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a,b = s[:len(s)//2], s[len(s)//2:]
        a = [c.lower() for c in a]
        b = [c.lower() for c in b]
        
        return a.count('a')+a.count('e')+a.count('i')+a.count('o')+a.count('u')==b.count('a')+b.count('e')+b.count('i')+b.count('o')+b.count('u')
