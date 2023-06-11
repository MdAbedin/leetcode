class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        dividend,divisor = map(abs,[dividend,divisor])
        ans = 0

        while dividend >= divisor:
            quotient = 1
            product = divisor

            while (product<<1) <= dividend:
                product <<= 1
                quotient <<= 1

            dividend -= product
            ans += quotient

        return max(-2147483648, min(2147483647, ans * (-1 if negative else 1)))
