class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens,closes = "({[",")}]"

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack or stack[-1] != opens[closes.find(c)]: return False
                stack.pop()

        return not stack
