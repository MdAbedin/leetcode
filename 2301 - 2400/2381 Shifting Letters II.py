class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ps = [0]*(len(s)+1)

        for l,r,d in shifts:
            ps[l] += [-1,1][d]
            ps[r+1] -= [-1,1][d]

        return "".join(ascii_lowercase[(ord(c)-ord("a")+shift)%26] for c,shift in zip(s,accumulate(ps)))
