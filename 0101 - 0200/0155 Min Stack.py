class MinStack:
    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append((val,min(val,self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
