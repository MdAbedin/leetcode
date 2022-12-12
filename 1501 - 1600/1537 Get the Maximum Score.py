class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        cur1 = len(nums1)-1
        cur2 = len(nums2)-1
        ans = 0
        dp = dict()
        
        while cur1 >= 0 or cur2 >= 0:
            if cur1 >= 0 and cur2 >= 0 and nums1[cur1] == nums2[cur2]:
                dp[nums1[cur1]] = max(dp[nums1[cur1+1]] if cur1+1 < len(nums1) else 0, dp[nums2[cur2+1]] if cur2+1 < len(nums2) else 0) + nums1[cur1]
                ans = max(ans, dp[nums1[cur1]])
                cur1 -= 1
                cur2 -= 1
            else:
                if cur2 < 0 or (cur1 >= 0 and nums1[cur1] > nums2[cur2]):
                    dp[nums1[cur1]] = nums1[cur1] + (dp[nums1[cur1+1]] if cur1+1 < len(nums1) else 0)
                    ans = max(ans, dp[nums1[cur1]])
                    cur1 -= 1
                else:
                    dp[nums2[cur2]] = nums2[cur2] + (dp[nums2[cur2+1]] if cur2+1 < len(nums2) else 0)
                    ans = max(ans, dp[nums2[cur2]])
                    cur2 -= 1
        
        return int(ans%(1e9+7))
