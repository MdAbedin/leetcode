class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        befores = defaultdict(list)
        
        for i in range(len(t)):
          befores[t[i]].insert(0,i)

        founds = defaultdict(int)
        founds[0] = 1

        for i in range(len(s)):
            for before in befores[s[i]]:
                founds[before+1] += founds[before]

        return founds[len(t)]
