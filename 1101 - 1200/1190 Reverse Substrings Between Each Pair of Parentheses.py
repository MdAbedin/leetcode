class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for c in s:
            if c == "(":
                stack.append([])
            elif c == ")":
                l = stack.pop()[::-1]
                stack[-1] += l
            else:
                stack[-1].append(c)

        return "".join(stack[-1])
