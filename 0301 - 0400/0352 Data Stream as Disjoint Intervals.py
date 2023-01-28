class SummaryRanges:
    def __init__(self):
        self.nums = [False] * (10**4 + 1)
        self.ans = []

    def addNum(self, value: int) -> None:
        if self.nums[value]: return
        
        self.nums[value] = True
        left_exists = value-1 >= 0 and self.nums[value-1]
        right_exists = value+1 < len(self.nums) and self.nums[value+1]
        
        if left_exists and right_exists:
            i = bisect_right(self.ans, [value,value])-1
            self.ans[i][1] = self.ans[i+1][1]
            self.ans.pop(i+1)
        elif left_exists:
            self.ans[bisect_right(self.ans, [value,value])-1][1] = value
        elif right_exists:
            self.ans[bisect_right(self.ans, [value,value])][0] = value
        else:
            insort(self.ans, [value,value])

    def getIntervals(self) -> List[List[int]]:
        return self.ans
