class NestedIterator:
    def flatten(self,nested_list):
        return [nested_list.getInteger()] if nested_list.isInteger() else sum(map(self.flatten,nested_list.getList()),[])

    def __init__(self, nestedList: [NestedInteger]):
        self.nums = sum(map(self.flatten,nestedList),[])
        self.i = 0

    def next(self) -> int:
        self.i += 1
        return self.nums[self.i-1]
    
    def hasNext(self) -> bool:
        return self.i < len(self.nums)
