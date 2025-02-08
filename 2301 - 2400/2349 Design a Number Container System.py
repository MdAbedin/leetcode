from sortedcontainers import SortedList

class NumberContainers:
    def __init__(self):
        self.sls = defaultdict(SortedList)
        self.nums = {}

    def change(self, index: int, number: int) -> None:
        if index in self.nums: self.sls[self.nums[index]].remove(index)
        self.sls[number].add(index)
        self.nums[index] = number
        
    def find(self, number: int) -> int:
        return -1 if not self.sls[number] else self.sls[number][0]
