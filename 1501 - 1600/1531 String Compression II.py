class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def solve(i,k):
            ans1,ans2 = 1 if len(s)-i-1 <= k else inf,1

            for i2 in range(i+1,min(i+k+2,len(s))):
                cur_ans1,cur_ans2 = solve(i2,k-(i2-i-1))

                if s[i2] == s[i]:
                    cur_ans1 += cur_ans2 == 1 or set(str(cur_ans2)) == {"9"}
                    cur_ans2 += 1
                else:
                    cur_ans1 += 1
                    cur_ans2 = 1

                if cur_ans1 < ans1 or (cur_ans1 == ans1 and cur_ans2 > ans2): ans1,ans2 = cur_ans1,cur_ans2

            return ans1,ans2

        return 0 if k == len(s) else min(solve(i,k-i)[0] for i in range(min(k+1,len(s))))
