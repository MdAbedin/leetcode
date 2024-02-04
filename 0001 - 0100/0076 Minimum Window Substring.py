class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)

        def solve(l):
            c = Counter()

            for i in range(len(s)):
                c[s[i]] += 1
                if all(c[ch] >= count for ch,count in ct.items()): return True,s[i-l+1:i+1]
                if i-l+1 >= 0: c[s[i-l+1]] -= 1

            return False,""

        return solve(bisect_left(range(1,len(s)+1),(True,""),key=solve)+1)[1]
