class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            if stack[-len(part):] == list(part): stack = stack[:-len(part)]

        return "".join(stack)
