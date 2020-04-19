class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        alphas = []
        
        for c in s:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                nums.append(c)
            else:
                alphas.append(c)
            
        if abs(len(nums)-len(alphas)) > 1:
            return ""
        
        ans = ""
        
        for i in range(min(len(nums), len(alphas))):
            if len(nums) > len(alphas):
                ans += nums[i]
                ans += alphas[i]
            else:
                ans += alphas[i]
                ans += nums[i]
            
        ans += alphas[-1] if len(alphas) > len(nums) else ''
        ans += nums[-1] if len(nums) > len(alphas) else ''
        
        return ans
