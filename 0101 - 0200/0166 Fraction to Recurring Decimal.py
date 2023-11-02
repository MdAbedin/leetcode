class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        result = [('-' if numerator*denominator < 0 else '') + str(n), '.']
        stack = []

        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(2+idx,'(')
        result.append(')')

        return ''.join(result).replace('(0)','').rstrip('.')
