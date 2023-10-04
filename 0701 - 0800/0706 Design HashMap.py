class MyHashMap:
    def __init__(self):
        self.table = [-1]*(10**6+1)

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        return self.table[key]

    def remove(self, key: int) -> None:
        self.table[key] = -1
