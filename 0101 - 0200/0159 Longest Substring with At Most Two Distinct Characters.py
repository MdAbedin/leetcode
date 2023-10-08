class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts = Counter()
        r = 0
        ans = 0

        for l in range(len(s)):
            while r < len(s) and (len(counts) < 2 or s[r] in counts):
                counts[s[r]] += 1
                r += 1

            ans = max(ans,r-l)
            counts[s[l]] -= 1
            if counts[s[l]] == 0: counts.pop(s[l])

        return ans
