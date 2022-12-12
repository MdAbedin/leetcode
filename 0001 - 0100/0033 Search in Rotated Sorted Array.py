class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums)-1
        left_segment_end = 0
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] >= nums[0]:
                left_segment_end = mid
                l = mid+1
            else:
                r = mid-1
        
        l, r = 0, left_segment_end
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        l, r = left_segment_end+1, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return -1
