class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = bisect_left(nums,target)
        return ans if ans < len(nums) and nums[ans] == target else -1
