class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        for left,right in zip(l,r):
            subarray_set = set(nums[left:right+1])
            min_num, max_num = min(subarray_set), max(subarray_set)
            d = (max_num - min_num) / (right - left)

            ans.append(all(min_num + i*d in subarray_set for i in range(right - left)))

        return ans
