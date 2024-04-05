class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c.isalpha() and stack[-1] == c.swapcase(): stack.pop()
            else: stack.append(c)

        return "".join(stack)
