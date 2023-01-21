class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        for i1,i2,i3 in combinations(range(1,len(s)), 3):
            nums = [s[:i1], s[i1:i2], s[i2:i3], s[i3:]]
            
            if all(0 <= int(num) <= 255 and (num[0] != "0" or num == "0") for num in nums):
                ans.append(".".join(nums))
            
        return ans
