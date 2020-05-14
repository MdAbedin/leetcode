class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1, self.v2 = v1, v2
        self.i1 = self.i2 = 0
        self.on_1 = len(v1) > 0

    def next(self) -> int:
        ans = 0
        
        if self.on_1:
            ans = self.v1[self.i1]
            self.i1 += 1
            
            self.on_1 = self.i2 == len(self.v2)
        else:
            ans = self.v2[self.i2]
            self.i2 += 1
            
            self.on_1 = self.i1 != len(self.v1)
            
        return ans

    def hasNext(self) -> bool:
        return self.i1+self.i2 < len(self.v1)+len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
