class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_inds = {0:-1}
        ans = ps = 0

        for i,num in enumerate(nums):
            ps += 1 if num == 1 else -1
            if ps in first_inds: ans = max(ans,i-first_inds[ps])
            else: first_inds[ps] = i

        return ans
