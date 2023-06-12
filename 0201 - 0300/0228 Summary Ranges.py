class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        for num in nums:
            if ans and num==ans[-1][1]+1: ans[-1][1] = num
            else: ans.append([num,num])

        return [str(l) if l==r else f"{l}->{r}" for l,r in ans]
