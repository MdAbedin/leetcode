class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        ans = 0
        
        for num in nums:
            ans += sl.bisect_right(upper-num)-sl.bisect_left(lower-num)
            sl.add(num)

        return ans
