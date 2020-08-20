class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = nums[0], nums[0]
        ans = nums[0]
        
        for num in nums[1:]:
            mx, mn = max(num, mx*num, mn*num), min(num, mx*num, mn*num)
            ans = max(ans, mx)
            
        return ans
