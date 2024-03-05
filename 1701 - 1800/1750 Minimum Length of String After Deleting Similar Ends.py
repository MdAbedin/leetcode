class Solution:
    def minimumLength(self, s: str) -> int:
        groups = [list(g) for k,g in groupby(s)]
        ans = len(s)

        for i in range(ceil(len(groups)/2)):
            if groups[i][0] != groups[~i][0]: break

            if i == len(groups)//2: ans -= 0 if len(groups[len(groups)//2]) == 1 else len(groups[len(groups)//2])
            else: ans -= len(groups[i])+len(groups[~i])
            

        return ans
