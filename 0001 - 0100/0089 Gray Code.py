class Solution:
    def grayCode(self, n):
        seen = {0}
        ans = [0]

        while len(ans) < 2**n:
            for i in range(n):
                if ans[-1]^(1<<i) not in seen:
                    seen.add(ans[-1]^(1<<i))
                    ans.append(ans[-1]^(1<<i))
                    break
                    
        return ans
