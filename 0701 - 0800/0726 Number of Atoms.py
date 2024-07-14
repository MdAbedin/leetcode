class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i = 0
        stack = [Counter()]

        while i < len(formula):
            if formula[i] == "(":
                stack.append(Counter())
                i += 1
            elif formula[i] == ")":
                if i+1 == len(formula) or not formula[i+1].isdigit():
                    counts = stack.pop()
                    stack[-1] += counts
                i += 1
            elif formula[i].isalpha():
                atom = [formula[i]]
                i += 1
                count = 0

                while i < len(formula) and formula[i].islower():
                    atom.append(formula[i])
                    i += 1

                while i < len(formula) and formula[i].isdigit():
                    count = count*10 + int(formula[i])
                    i += 1

                if not count: count = 1
                stack[-1]["".join(atom)] += count
            elif formula[i].isdigit():
                counts = stack.pop()
                m = 0

                while i < len(formula) and formula[i].isdigit():
                    m = m*10 + int(formula[i])
                    i += 1

                if not m: m = 1
                for atom in counts: counts[atom] *= m
                stack[-1] += counts

        return "".join(f"{a}{'' if c == 1 else c}" for a,c in sorted(stack[0].items()))
