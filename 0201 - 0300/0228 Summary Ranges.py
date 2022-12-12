class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        
        ans = []
        prev_start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] == prev_start:
                    ans.append(str(prev_start))
                else:
                    ans.append(f"{prev_start}->{nums[i-1]}")
                
                prev_start = nums[i]

        if prev_start == nums[-1]:
            ans.append(str(prev_start))
        else:
            ans.append(f"{prev_start}->{nums[-1]}")

        return ans
