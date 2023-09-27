class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        def solve(i):
            l = 0

            for c in s:
                if c.isalpha():
                    if l == i: return c
                    l += 1
                else:
                    if l*int(c) > i: return solve(i%l)
                    l *= int(c)

        return solve(k-1)
