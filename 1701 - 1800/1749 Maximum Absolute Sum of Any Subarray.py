class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m1,m2 = 0,0
        s = 0
        ans = 0

        for num in nums:
            s += num
            ans = max(ans,abs(s-m1),abs(s-m2))
            m1,m2 = min(m1,s),max(m2,s)

        return ans
