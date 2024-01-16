class RandomizedSet:
    def __init__(self):
        self.l = []
        self.inds = {}

    def insert(self, val: int) -> bool:
        if val not in self.inds:
            self.l.append(val)
            self.inds[val] = len(self.l)-1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.inds:
            self.inds[self.l[-1]] = self.inds[val]
            self.l[self.inds[val]],self.l[-1] = self.l[-1],self.l[self.inds[val]]
            self.inds.pop(self.l.pop())
            return True
        
        return False

    def getRandom(self) -> int:
        return choice(self.l)
