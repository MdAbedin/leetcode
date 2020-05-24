class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        ans = nums1[0]*nums2[0]
        dp = [[0]*len(nums2) for e in nums1]
        dp[0][0] = ans
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                possibles = []
                if i-1>=0 and j-1>= 0: possibles.append(dp[i-1][j-1])
                if i-1>=0 and j-1>= 0: possibles.append(nums1[i]*nums2[j] + max(0, dp[i-1][j-1]))                
                if i-1>=0: possibles.append(dp[i-1][j])
                if j-1>=0: possibles.append(dp[i][j-1])
                possibles.append(nums1[i]*nums2[j])
                
                dp[i][j] = max(possibles)
                ans = max(ans,dp[i][j])
                    
        return ans
