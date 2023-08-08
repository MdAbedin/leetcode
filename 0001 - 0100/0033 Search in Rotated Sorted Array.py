class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target: return m

            if nums[m] <= nums[-1]:
                if nums[m] < target <= nums[-1]: l = m+1
                else: r = m-1
            else:
                if nums[0] <= target < nums[m]: r = m-1
                else: l = m+1

        return -1
