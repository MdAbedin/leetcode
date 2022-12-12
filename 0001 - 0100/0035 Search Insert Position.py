class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = (l+r)//2
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target: return mid
            if nums[mid] > target: r = mid-1
            if nums[mid] < target: l = mid+1
                
        return ceil((l+r)/2)
