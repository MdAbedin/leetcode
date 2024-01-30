class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t in "+-*/": s.append(str(int(eval(t.join([s.pop(-2),s.pop()])))))
            else: s.append(t)

        return int(s[0])
