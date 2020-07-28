class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        dp = [[1,-1] for num in nums]
        ans_len, ans_i = 1, 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = [max(dp[i][0], dp[j][0]+1), j if max(dp[i][0], dp[j][0]+1) > dp[i][0] else dp[i][1]]
                    
                    if dp[i][0] > ans_len:
                        ans_len = dp[i][0]
                        ans_i = i
                        
        ans = set()
        while ans_i != -1:
            ans.add(nums[ans_i])
            ans_i = dp[ans_i][1]
            
        return list(ans)
