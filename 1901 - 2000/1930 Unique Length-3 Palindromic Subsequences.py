class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        inds = {c:[s.find(c)+1,s.rfind(c)] for c in ascii_lowercase}
        return len({c2+c+c2 for i,c in enumerate(s) for c2 in ascii_lowercase if i in range(*inds[c2])})
