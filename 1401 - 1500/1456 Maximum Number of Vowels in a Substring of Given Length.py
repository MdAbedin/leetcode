class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        ans,cur_ans = 0,0

        for i,c in enumerate(s):
            if c in vowels: cur_ans += 1
            if i-k >= 0 and s[i-k] in vowels: cur_ans -= 1
            ans = max(ans,cur_ans)

        return ans
