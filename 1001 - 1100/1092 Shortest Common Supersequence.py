class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def solve(i1,i2):
            if i1 == len(str1) or i2 == len(str2): return len(str1)-i1 + len(str2)-i2
            return 1 + (solve(i1+1,i2+1) if str1[i1] == str2[i2] else min(solve(i1+1,i2),solve(i1,i2+1)))

        i1,i2 = 0,0
        ans = []

        while i1 < len(str1) and i2 < len(str2):
            if str1[i1] == str2[i2]:
                ans.append(str1[i1])
                i1 += 1
                i2 += 1
            elif solve(i1+1,i2) < solve(i1,i2+1):
                ans.append(str1[i1])
                i1 += 1
            else:
                ans.append(str2[i2])
                i2 += 1

        return "".join(ans) + str1[i1:] + str2[i2:]
