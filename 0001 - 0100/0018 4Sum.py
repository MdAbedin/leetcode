class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = Counter(nums)
        ans = set()
        
        for i in range(len(nums)):
            counts[nums[i]] -= 1
            
            for j in range(i):
                for k in range(j):
                    if counts[target-nums[i]-nums[j]-nums[k]] > 0:
                        ans.add(tuple(sorted([nums[i],nums[j],nums[k],target-nums[i]-nums[j]-nums[k]])))
                        
        return list(ans)
