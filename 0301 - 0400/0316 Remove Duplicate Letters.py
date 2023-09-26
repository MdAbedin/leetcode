class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        final_inds = {c:s.rfind(c) for c in set(s)}
        ans = []
        start = 0

        while final_inds:
            end = min(final_inds.values())
            c,i = min((c,i) for c in final_inds if (i := s.find(c,start,end+1)) != -1)
            ans.append(c)
            final_inds.pop(c)
            start = i+1

        return "".join(ans)
