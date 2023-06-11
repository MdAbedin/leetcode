class SnapshotArray:
    def __init__(self, length: int):
        self.history = defaultdict(lambda: [[-1,0]])
        self.updates = {}
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        self.updates[index] = val

    def snap(self) -> int:
        for index,val in self.updates.items(): self.history[index].append([self.snaps,val])

        self.updates = {}
        self.snaps += 1

        return self.snaps-1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.history[index], [snap_id,inf])-1
        return self.history[index][i][1]
