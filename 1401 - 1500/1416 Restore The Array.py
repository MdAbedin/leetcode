class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:

        MOD = 10**9+7

        

        @cache

        def solve(i):

            if i == len(s): return 1

            if s[i] == "0": return 0

            

            ans = 0

            num = 0

            

            for j in range(i,min(len(s),i+10)):

                num *= 10

                num += int(s[j])

                

                if num > k: break

                    

                ans += solve(j+1)

                ans %= MOD

                

            return ans

        

        return solve(0)

            
