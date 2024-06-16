class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m,ans = 0,0
        nums.sort(reverse=True)

        while m < n:
            if nums and nums[-1] <= m+1:
                m += nums.pop()
            else:
                m += m+1
                ans += 1

        return ans
