class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = -1
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                left = mid
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
        
        right = -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                right = mid
            if nums[mid] <= target:
                l = mid+1
            else:
                r = mid-1
        
        return False if left == -1 and right == -1 else right-left+1 > len(nums)/2
