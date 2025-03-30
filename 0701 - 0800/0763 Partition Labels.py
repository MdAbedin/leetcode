class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        end = -1

        for i,c in enumerate(s):
            end = max(end,s.rfind(c))
            if i == end: ans.append(end-sum(ans)+1)

        return ans
