class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l_counts,r_counts = Counter(),Counter(nums)
        ans = set()

        for num2 in nums:
            r_counts[num2] -= 1

            for num1 in l_counts:
                num3 = 0-num1-num2
                if r_counts[num3] > 0: ans.add(tuple(sorted([num1,num2,num3])))

            l_counts[num2] += 1
            
        return ans
