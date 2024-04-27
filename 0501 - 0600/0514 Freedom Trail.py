class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def solve(i,i2): return 0 if i2 == len(key) else 1+min(min(abs(i3-i),len(ring)-abs(i3-i))+solve(i3,i2+1) for i3,c in enumerate(ring) if c == key[i2])
        return solve(0,0)
