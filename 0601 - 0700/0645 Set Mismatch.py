class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=b=0
        counts = Counter(nums)

        for num in range(1,len(nums)+1):
            if counts[num] == 2: a = num
            if counts[num] == 0: b = num

        return a,b
