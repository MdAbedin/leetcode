class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = -inf

        for val in preorder:
            if val < lower_bound: return False
            while stack and stack[-1] < val: lower_bound = stack.pop()
            stack.append(val)

        return True
