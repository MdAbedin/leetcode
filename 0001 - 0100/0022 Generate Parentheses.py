class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def works(s):
            level = 0

            for c in s:
                if c == "(":
                    level += 1
                else:
                    level -= 1
                    if level < 0: return False

            return level == 0

        return [s for num in range(2**(2*n)) if works(s := "".join("()"[num&(1<<i)!=0] for i in range(2*n)))]
