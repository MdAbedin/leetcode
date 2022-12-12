class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace("(", " ( ")
        s = s.replace(")", " ) ")
        s = s.replace("+", " + ")
        s = s.replace("-", " - ")
        terms = s.split()
        for i,term in enumerate(terms):
            if term.isdigit(): terms[i] = int(terms[i])
        stack = []
        
        for term in terms:
            if term == "(":
                stack.append("(")
            elif term == ")":
                num = stack.pop()
                stack.pop()
                stack.append(num)
            elif term in ["+", "-"]:
                stack.append(term)
            else:
                stack.append(term)
                
            if len(stack) >= 2 and isinstance(stack[-1], int) and stack[-2] in ["+", "-"]:
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()

                if op == "+":
                    stack.append(num1 + num2)
                else:
                    stack.append(num1 - num2)

        return stack[0]
