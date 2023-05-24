class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        right_nums = sorted(nums)
        ans = -inf

        for i in range(len(nums)):
            right_nums.remove(nums[i])

            for j in range(i):
                k = bisect_right(right_nums,target-nums[i]-nums[j])
                for k in [k-1,k]:
                    if k in range(len(right_nums)) and abs(target-(nums[i]+nums[j]+right_nums[k])) < abs(target-ans): ans = nums[i]+nums[j]+right_nums[k]

        return ans
