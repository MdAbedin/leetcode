class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = sorted(nums)[len(nums)//2]
        c1,c2 = 0,nums.count(d)

        for i,num in enumerate(nums):
            c1 += num == d
            c2 -= num == d
            if c1 > (i+1)//2 and c2 > (len(nums)-1-i)//2: return i

        return -1
