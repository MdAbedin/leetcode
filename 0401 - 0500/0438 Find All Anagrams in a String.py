class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1 = Counter(p)
        c2 = Counter(s[:len(p)-1])
        ans = []

        for i in range(len(p)-1,len(s)):
            c2[s[i]] += 1
            if c2 == c1: ans.append(i-len(p)+1)
            c2[s[i-len(p)+1]] -= 1

        return ans
