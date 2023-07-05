class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = [0]
        for num in nums[:-1]:
            if num == 1: l.append(l[-1]+1)
            else: l.append(0)

        r = [0]
        for num in nums[::-1][:-1]:
            if num == 1: r.append(r[-1]+1)
            else: r.append(0)

        r.reverse()

        return max((ls+rs for ls,rs in zip(l,r)),default=0)
