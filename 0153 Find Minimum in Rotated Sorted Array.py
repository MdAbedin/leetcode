class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        ans = -1
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] <= nums[-1]:
                ans = nums[mid]
                r = mid-1
            else:
                l = mid+1
                
        return ans
