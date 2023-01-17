class Solution:
    def reverse(self, x: int) -> int:
        ans = int(copysign(int(str(abs(x))[::-1]), x))
        return 0 if ans not in range(-2**31, 2**31) else ans
