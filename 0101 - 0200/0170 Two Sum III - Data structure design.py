class TwoSum:
    def __init__(self):
        self.counts = Counter()

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        return any(self.counts[value-num] >= (2 if num == value-num else 1) for num in self.counts)
