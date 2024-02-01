class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.s = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size: self.s -= self.queue.popleft()
        
        self.queue.append(val)
        self.s += val

        return self.s/len(self.queue)
