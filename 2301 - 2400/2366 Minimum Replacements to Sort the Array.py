class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        next_num = inf
        ans = 0

        for num in nums[::-1]:
            if num > next_num:
                split_count = ceil(num/next_num)
                next_num = num//split_count
                ans += split_count-1
            else:
                next_num = num

        return ans
