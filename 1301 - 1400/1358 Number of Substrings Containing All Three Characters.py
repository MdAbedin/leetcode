class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = Counter()
        i = 0
        ans = 0

        for char in s:
            while i < len(s) and len(counts) < 3:
                counts[s[i]] += 1
                i += 1

            if len(counts) == 3: ans += len(s)-i+1
            counts[char] -= 1
            if counts[char] == 0: counts.pop(char)

        return ans
