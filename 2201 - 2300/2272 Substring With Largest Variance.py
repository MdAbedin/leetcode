class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        counts = Counter(s)

        for max_c,min_c in permutations(ascii_lowercase,2):
            cur_ans = 0
            has_max,has_min = False,False
            min_left = counts[min_c]

            for c in s:
                if c == max_c:
                    cur_ans += 1
                    has_max = True
                    
                if c == min_c:
                    cur_ans -= 1
                    has_min = True
                    min_left -= 1

                if cur_ans < 0 and min_left > 0:
                    cur_ans = 0
                    has_max,has_min = False,False

                if has_max and has_min: ans = max(ans,cur_ans)

        return ans
