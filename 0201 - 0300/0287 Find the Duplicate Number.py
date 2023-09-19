class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow,fast = nums[slow],nums[nums[fast]]
            if slow == fast: break
        
        slow = nums[0]

        while slow != fast: slow,fast = nums[slow],nums[fast]
        
        return fast
