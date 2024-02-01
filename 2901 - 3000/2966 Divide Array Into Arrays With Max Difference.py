class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [nums[i:i+3] for i in range(0,len(nums),3)]

        return ans if all(l[2]-l[0] <= k for l in ans) else []
